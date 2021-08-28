from passlib.hash import sha256_crypt


def hash_password(plain_text):
    hashed_password = sha256_crypt.encrypt(plain_text)
    return hashed_password
