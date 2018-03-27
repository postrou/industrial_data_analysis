"""
This file is a python script, using given Regression model to predict some results
"""

import sys
import pickle
import numpy as np

from model import RegressionModel


def main(model_filename, X_filename):
    """
    Call `predict` method from fitted `model` and save results to `result.txt`
    :param model_filename: filename of saved model
    :param X_filename: object-feature predict matrix
    """
    X = np.loadtxt(X_filename)

    with open(model_filename, 'rb') as f:
        model = pickle.load(f)

    result = model.predict(X)
    np.savetxt('result.txt', result)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])