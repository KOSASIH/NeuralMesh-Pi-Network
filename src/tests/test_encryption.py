import unittest
from src.encryption import Encryption

class TestEncryption(unittest.TestCase):
    def test_init(self):
        encryption = Encryption()
        self.assertIsInstance(encryption, Encryption)

    def test_encrypt(self):
        encryption = Encryption()
        data = 'secret data'
        encrypted_data = encryption.encrypt(data)
        self.assertNotEqual(data, encrypted_data)

    def test_decrypt(self):
        encryption = Encryption()
        data = 'secret data'
        encrypted_data = encryption.encrypt(data)
        decrypted_data = encryption.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
