"""
This file is a python script, fitting a model, given as an argument
"""

import sys
import pickle

from .model import RegressionModel


def main(X, y, filename):
    """
    Init RegressionModel object and call `fit` method with corresponding arguments and save it as `pickle`
    :param X: object-feature learn matrix
    :param y: `y` values form `f(X) = y`
    :param filename: name of file to save model
    """
    model = RegressionModel()
    model.fit(X, y)
    with open(filename, 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
