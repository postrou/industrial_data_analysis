import os
import pickle

import boto3
import numpy as np
from flask import Flask, request

from flask_ddb import model_ddb, data_ddb
from model import RegressionModel

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = 'txt'

app = Flask(__name__)

dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

models_table_name = 'Models'
data_table_name = 'Data'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return


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
    X_file_path = os.path.join(current_dir, '../check/' + X_file.filename)
    y_file_path = os.path.join(current_dir, '../check/' + y_file.filename)

    X_file.save(X_file_path)
    y_file.save(y_file_path)

    X = np.loadtxt(X_file_path)
    y = np.loadtxt(y_file_path)

    model = RegressionModel()
    model.fit(X, y)
    model_bytes = pickle.dumps(model)
    with open(os.path.join(current_dir, '../check/regression_model.pkl'), 'wb') as f:
        f.write(model_bytes)

    existing_tables = dynamodb.list_tables()['TableNames']
    if models_table_name not in existing_tables:
        model_ddb.create_table(dynamodb)
    # else:
    #     table = dynamodb.Table(models_table_name)
    request_url = request.url
    model_ddb.add_model_to_db(dynamodb, models_table_name, model_bytes, request_url)

    return 'ok'


@app.route('/app/predict/<path:data_filename>', methods=['GET'])
def predict():

    return


if __name__ == '__main__':
    app.run()
