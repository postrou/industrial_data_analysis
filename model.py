import numpy as np
from sklearn.linear_model import LinearRegression


class RegressionModel(object):

    """
    Regression model class.

    As regression model the linear regression from scikit-learn was taken. Takes nothing as input.
    """

    def __init__(self):
        """
        Initialize a `RegressionModel` object.
        """

        self.model = LinearRegression(n_jobs=4)

    def fit(self, X, y):
        """
        Fit method, uses standard fit function from scikit-learn.

        **Parameters**:

        - `X`: object-feature learn matrix
        - `y`: `y` values form `f(X) = y`
        """

        for j in range(X.shape[1]):
            if np.array_equal(X[:, j], y):
                raise ValueError
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predict method, uses standard predict function from scikit-learn, returning predicted results

        **Parameters**:

        - `X`: object-feature predict matrix
        """

        return self.model.predict(X)
