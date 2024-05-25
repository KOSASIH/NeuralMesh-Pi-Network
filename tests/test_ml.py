import unittest
from src.ml import NeuralNetwork

class TestML(unittest.TestCase):
    def test_init(self):
        nn = NeuralNetwork((10,), 2)
        self.assertIsInstance(nn, NeuralNetwork)

    def test_train(self):
        nn = NeuralNetwork((10,), 2)
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 2, 100)
        nn.train(X, y)

    def test_predict(self):
        nn = NeuralNetwork((10,), 2)
        X = np.random.rand(100, 10)
        nn.train(X, np.random.randint(0, 2, 100))
        y_pred = nn.predict(X)
        self.assertEqual(y_pred.shape, (100, 2))

if __name__ == '__main__':
    unittest.main()
