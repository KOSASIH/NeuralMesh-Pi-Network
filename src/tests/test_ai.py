import unittest
from src.ai import AI

class TestAI(unittest.TestCase):
    def test_init(self):
        ai = AI()
        self.assertIsInstance(ai, AI)

    def test_make_decision(self):
        ai = AI()
        decision = ai.make_decision()
        self.assertIsInstance(decision, str)

if __name__ == '__main__':
    unittest.main()
