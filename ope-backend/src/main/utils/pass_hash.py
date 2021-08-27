import hashlib


def hash_password(plain_text):
    SALT_KEY = "jiaJjns8Oi/2Eew0008"
    salted_password = plain_text + SALT_KEY
    hashed_password = hashlib.sha256(salted_password.encode())
    return hashed_password.hexdigest()
