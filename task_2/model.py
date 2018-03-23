

from sklearn.linear_model import LinearRegression


class RegressionModel(object):

    def __init__(self):
        self.model = LinearRegression(n_jobs=4)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        self.model.predict(X)
