import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()
encrypted_password = os.getenv('PASSWORD')
key = os.getenv('KEY')

def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(
        encrypted_password.encode()).decode()
    return decrypted_password

# Get default password from env file
def get_password():
    if not key or not encrypted_password:
        raise ValueError('Encryption key or encrypted password '\
                         'is missing from the environment variables.')
    try:
        decrypted_password = decrypt_password(
            key.encode(), encrypted_password) 
        return decrypted_password
    except Exception as e:
        raise ValueError(f'Failed to decrypt password: {e}')
