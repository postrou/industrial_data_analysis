"""
This file is a python script, using given Regression model to predict some results
"""

import sys
import pickle
import numpy as np

from model import RegressionModel


def main(X_filename, model_filename):
    """
    Call `predict` method from fitted `model` and save results to `result.txt`
    :param X_filename: object-feature predict matrix
    :param model_filename: filename of saved model
    """
    X = np.loadtxt(X_filename)

    with open(model_filename, 'rb') as f:
        model = pickle.load(f)

    result = model.predict(X)
    np.savetxt('result.txt', result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])