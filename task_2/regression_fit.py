"""
This file is a python script, fitting a model, given as an argument
"""

import sys
import pickle
import numpy as np

from model import RegressionModel


def main(X_filename, y_filename, model_filename):
    """
    Init RegressionModel object and call `fit` method with corresponding arguments and save it as `pickle`
    :param X_filename: filename where object-feature matrix is saved
    :param y_filename: filename of `y` values form `f(X) = y`
    :param model_filename: name of file to save model
    """
    X = np.loadtxt(X_filename)
    y = np.loadtxt(y_filename)

    reg_model = RegressionModel()
    reg_model.fit(X, y)

    with open(model_filename, 'wb') as f:
        pickle.dump(reg_model, f)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
