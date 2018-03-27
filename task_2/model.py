from sklearn.linear_model import LinearRegression


class RegressionModel(object):

    """
    Regression model class.

    As regression model the linear regression from scikit-learn wast taken. Takes nothing as input.
    """

    def __init__(self):
        """
        Initialize a `RegressionModel` object.
        """
        self.model = LinearRegression(n_jobs=4)

    def fit(self, X, y):
        """
        Fit method, uses standard fit function from scikit-learn.
        :param X: object-feature learn matrix
        :param y: `y` values form `f(X) = y`
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predict method, uses standard predict function from scikit-learn
        :param X: object-feature predict matrix
        """
        return self.model.predict(X)
