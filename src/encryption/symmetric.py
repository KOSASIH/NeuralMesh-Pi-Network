**symmetric.py**
```python
import os
import base64
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_data(key, data):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data

def encrypt_file(key, file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = encrypt_data(key, data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(key, file_path):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = decrypt_data(key, encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
