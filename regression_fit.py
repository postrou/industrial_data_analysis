"""
This file is a python script, fitting a model, given as an argument
"""

import sys
import pickle
import numpy as np
import json
import codecs


from model import RegressionModel


def main(X_filename='data/X_train.json', y_filename='data/y_train.json', model_filename='regression_model.pkl'):
    """
    Init RegressionModel object and call `fit` method with corresponding arguments and save it as `pickle`.

    **Parameters**:

    - `X_filename`: filename where object-feature matrix is saved
    - `y_filename`: filename of `y` values form `f(X) = y`
    - `model_filename`: name of file to save model
    """

    X = np.array(json.load(codecs.open(X_filename, 'r', encoding='utf-8')))
    y = np.array(json.load(codecs.open(y_filename, 'r', encoding='utf-8')))

    reg_model = RegressionModel()
    reg_model.fit(X, y)

    with open(model_filename, 'wb') as f:
        pickle.dump(reg_model, f)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
