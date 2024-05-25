import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = self.from_address + self.to_address + str(self.amount) + str(self.timestamp)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def sign_transaction(self, private_key):
        signer = serialization.load_pem_private_key(private_key, password=None)
        signature = signer.sign(self.hash.encode(), padding.PSS(mgf=padding.MGF1(algorithm=hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    def verify_transaction(self, public_key, signature):
        verifier = serialization.load_pem_public_key(public_key)
        verifier.verify(signature, self.hash.encode(), padding.PSS(mgf=padding.MGF1(algorithm=hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True
