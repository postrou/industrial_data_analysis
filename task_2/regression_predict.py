"""
This file is a python script, using given Regression model to predict some results
"""
import sys


def main(model, X):
    """
    Call `predict` method from fitted `model`
    :param model: fitted model object
    :param X: object-feature predict matrix
    :return: predicted results
    """
    result = model.predict(X)
    return result


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])