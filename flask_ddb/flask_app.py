import os
import pickle

import boto3
import numpy as np
from flask import Flask, request

from flask_ddb import model_ddb, data_ddb, request_ddb
from model import RegressionModel

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = 'txt'

app = Flask(__name__)

dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

models_table_name = 'Models'
data_table_name = 'Data'
requests_table_name = 'Requests'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# @app.route('/app/test', methods=['GET'])
# def test():
#     suite = unittest.TestLoader().loadTestsFromModule(test_project)
#     test_result = unittest.TextTestRunner(verbosity=2).run(suite)
#     if len(test_result.failures) != 0:
#         return test_result.failures[0][1]
#     return "ok!"


@app.route('/app/fit/', methods=['POST'])
def fit():
    X_file = request.files['X']
    y_file = request.files['y']

    if not (X_file and allowed_file(X_file.filename) and
            y_file and allowed_file(y_file.filename)):
        return 'something wrong'

    current_dir = os.path.dirname(os.path.realpath(__file__))
    X_file_path = os.path.join(current_dir, '../data/' + X_file.filename)
    y_file_path = os.path.join(current_dir, '../data/' + y_file.filename)

    X_file.save(X_file_path)
    y_file.save(y_file_path)

    X = np.loadtxt(X_file_path)
    y = np.loadtxt(y_file_path)

    model = RegressionModel()
    model.fit(X, y)
    model_bytes = pickle.dumps(model)
    with open(os.path.join(current_dir, '../data/regression_model.pkl'), 'wb') as f:
        f.write(model_bytes)

    existing_tables = dynamodb.list_tables()['TableNames']
    if models_table_name not in existing_tables:
        model_ddb.create_table(dynamodb)
    # else:
    #     dynamodb.delete_table(TableName=models_table_name)
    #     model_ddb.create_table(dynamodb)
    request_url = request.url
    model_ddb.add_model_to_db(dynamodb, models_table_name, model_bytes)

    if data_table_name not in existing_tables:
        data_ddb.create_table(dynamodb)
    # else:
    #     dynamodb.delete_table(TableName=data_table_name)
    #     data_ddb.create_table(dynamodb)
    data_ddb.add_fit_data_to_db(dynamodb,
                                data_table_name,
                                pickle.dumps(X),
                                pickle.dumps(y))

    if requests_table_name not in existing_tables:
        request_ddb.create_table(dynamodb)
    request_ddb.add_request_to_db(dynamodb,
                                  requests_table_name,
                                  request_url)

    return 'ok'


@app.route('/app/predict/', methods=['POST'])
def predict():
    X_file = request.files['X']

    if not (X_file and allowed_file(X_file.filename)):
        return 'something wrong'

    current_dir = os.path.dirname(os.path.realpath(__file__))
    X_file_path = os.path.join(current_dir, '../data/' + X_file.filename)

    X_file.save(X_file_path)

    X = np.loadtxt(X_file_path)

    model = pickle.loads(model_ddb.get_model_from_db(dynamodb,
                                                     models_table_name,
                                                     'linear_regression'))
    y_result = model.predict(X)

    return y_result


if __name__ == '__main__':
    app.run()
