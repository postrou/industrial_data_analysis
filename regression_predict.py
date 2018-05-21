"""
This file is a python script, using given Regression model to predict some results
"""

import sys
import pickle
import numpy as np
import json
import codecs


def main(X_filename='data/X_test.json', model_filename='data/regression_model.pkl'):
    """
    Call `predict` method from fitted `model` and save results to `result.txt`

    **Parameters**:

    - `X_filename`: object-feature predict matrix
    - `model_filename`: filename of saved model
    """
    X = np.array(json.load(codecs.open(X_filename, 'r', encoding='utf-8')))

    with open(model_filename, 'rb') as f:
        model = pickle.load(f)

    result = model.predict(X)
    json.dump(result.tolist(),
              codecs.open('data/result.json', 'w', encoding='utf-8'))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
