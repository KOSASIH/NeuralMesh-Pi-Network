import unittest
from src.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def test_init(self):
        blockchain = Blockchain()
        self.assertIsInstance(blockchain, Blockchain)

    def test_add_block(self):
        blockchain = Blockchain()
        blockchain.add_block('data')
        self.assertEqual(len(blockchain.chain), 2)

if __name__ == '__main__':
    unittest.main()
