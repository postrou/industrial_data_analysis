import unittest
import numpy as np
from sklearn.linear_model import LinearRegression

from model import RegressionModel


class RegressionModelTestCase(unittest.TestCase):

    def setUp(self):
        self.model = RegressionModel()

    def test_is_linear_regression_model(self):
        self.assertIsInstance(self.model.model, LinearRegression)

    def test_fit_X_and_y_wrong_dimensions(self):
        X = np.arange(1, 7).reshape(2, 3)
        y = np.ones(3)
        with self.assertRaises(ValueError):
            self.model.fit(X, y)

    def test_predict_correct_dimensions(self):
        X_train = np.eye(2)
        X_test = np.arange(1, 7).reshape(2, 3)
        y_train = np.ones(2)

        self.model.fit(X_train, y_train)

        with self.assertRaises(ValueError):
            result = self.model.predict(X_test)
            

if __name__ == '__main__':
    unittest.main()