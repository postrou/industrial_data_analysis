import os
import unittest
import numpy as np
import boto3
import pickle
from flask import Flask, request

from model import RegressionModel


UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = 'txt'

app = Flask(__name__)


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


@app.route('/app/test', methods=['GET'])
def test():
    suite = unittest.TestLoader().loadTestsFromModule(test_project)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(test_result.failures) != 0:
        return test_result.failures[0][1]
    return "ok!"


@app.route('/app/fit/', methods=['POST'])
def fit():
    # if 'file' not in request.files:
        # return "no file"

    X_file = request.files['X']
    y_file = request.files['y']

    #
    # if file and allowed_file(file.filename):
    #     filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    #     file.save(filepath)
    if not (X_file and allowed_file(X_file.filename) and y_file and allowed_file(y_file.filename)):
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
    with open(os.path.join(current_dir, '../data/regression_model.pkl'), 'wb') as f:
        pickle.dump(model, f)

    return 'ok'


@app.route('/app/predict/<path:data_filename>', methods=['GET'])
def predict(data_filename):
    return


if __name__ == '__main__':
    app.run()
