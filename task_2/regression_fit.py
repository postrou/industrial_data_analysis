"""
This file is a python script, fitting a model, given as an argument
"""

import sys

from task_2.model import RegressionModel


def main(X, y):
    """
    Init RegressionModel object and call `fit` method with corresponding arguments
    :param X: object-feature learn matrix
    :param y: `y` values form `f(X) = y`
    :return: fitted model
    """
    model = RegressionModel()
    model.fit(X, y)
    return model


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
