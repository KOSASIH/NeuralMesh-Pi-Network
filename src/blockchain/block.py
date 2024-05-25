**block.py**
```python
import hashlib
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + self.previous_hash + str(self.transactions) + str(self.timestamp) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def sign_block(self, private_key):
        signer = serialization.load_pem_private_key(private_key, password=None)
        signature = signer.sign(self.hash.encode(), padding.PSS(mgf=padding.MGF1(algorithm=hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    def verify_block(self, public_key, signature):
        verifier = serialization.load_pem_public_key(public_key)
        verifier.verify(signature, self.hash.encode(), padding.PSS(mgf=padding.MGF1(algorithm=hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True
