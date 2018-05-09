import unittest
from flask import Flask

import test_project


app = Flask(__name__)


@app.route('/app/test', methods=['GET'])
def test():
    suite = unittest.TestLoader().loadTestsFromModule(test_project)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(test_result.failures) != 0:
        return test_result.failures[0][1]
    return "ok!"

# @app.route('app/fit/<???>')
# def fit_model(data):



if __name__ == '__main__':
    app.run()