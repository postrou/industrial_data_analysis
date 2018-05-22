import os.path
import pickle
import sys

import boto3
import numpy as np
from flask import Flask, request, jsonify

import data_ddb
import model_ddb
import request_ddb

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from model import RegressionModel


app = Flask(__name__)


def init_model():
    if dynamodb.describe_table(TableName=models_table_name)['Table']['ItemCount'] == 0:
        return RegressionModel()
    else:
        return pickle.loads(model_ddb.get_model_from_db(dynamodb,
                                                        models_table_name,
                                                        'linear_regression'))


def create_tables():
    existing_tables = dynamodb.list_tables()['TableNames']

    if models_table_name not in existing_tables:
        model_ddb.create_table(dynamodb)
    # else:
    #     dynamodb.delete_table(TableName=models_table_name)
    #     model_ddb.create_table(dynamodb)

    if data_table_name not in existing_tables:
        data_ddb.create_table(dynamodb)
    # else:
    #     dynamodb.delete_table(TableName=data_table_name)
    #     data_ddb.create_table(dynamodb)

    if requests_table_name not in existing_tables:
        request_ddb.create_table(dynamodb)
    # else:
    #     dynamodb.delete_table(TableName=requests_table_name)
    #     request_ddb.create_table(dynamodb)


@app.route('/app/fit/', methods=['POST'])
def fit():
    if not request.is_json:
        return "NO JSON!"
    data = request.json
    X = np.array(data['X'])
    y = np.array(data['y'])

    model.fit(X, y)
    model_bytes = pickle.dumps(model)

    model_ddb.add_model_to_db(dynamodb,
                              models_table_name,
                              model_bytes)

    data_ddb.add_fit_data_to_db(dynamodb,
                                data_table_name,
                                pickle.dumps(X),
                                pickle.dumps(y))

    request_url = request.url
    request_ddb.add_request_to_db(dynamodb,
                                  requests_table_name,
                                  request_url)

    return 'ok'


@app.route('/app/predict/', methods=['PUT'])
def predict():
    if dynamodb.describe_table(TableName=models_table_name)['Table']['ItemCount'] == 0:
        return "table is empty"
    if not request.is_json:
        return "NO JSON!"
    X = np.array(request.json)

    data_ddb.add_predict_data_to_db(dynamodb,
                                    data_table_name,
                                    pickle.dumps(X))

    y_result = model.predict(X)

    return jsonify(result=y_result.tolist())


if __name__ == '__main__':
    dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

    models_table_name = 'Models'
    data_table_name = 'Data'
    requests_table_name = 'Requests'

    model = init_model()
    create_tables()
    app.run()
