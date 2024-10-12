import getpass
from cryptography.fernet import Fernet

def encrypt_password(password):
    try:
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encrypted_password = cipher_suite.encrypt(password.encode())
        return key, encrypted_password
    except Exception as e:
        raise ValueError(f'Encryption failed: {e}')

'''
# Prompt for password from the terminal
password = getpass.getpass(prompt='Enter your password: ')

# Encrypt the password
key, encrypted_password = encrypt_password(password)

# Save the key, and encrypted password to .env file
with open('../.env', 'a') as file:
    file.write(f'KEY={key.decode()}\n')
    file.write(f'PASSWORD={encrypted_password.decode()}\n')

print('Key and encrypted password have been written to .env')
'''