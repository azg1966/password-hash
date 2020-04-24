from hashlib import scrypt
from secrets import token_bytes, compare_digest


def _encrypt_password(password: bytes, salt: bytes):
    return scrypt(password, salt=salt, n=2048, r=16, p=8, dklen=32)


def generate_password(password: str) -> str:
    salt = token_bytes()
    hased_password = _encrypt_password(password.encode(), salt)
    return '{password}:{salt}'.format(password=hased_password.hex(),
                                      salt=salt.hex())


def check_password(password: str, stored_password: str) -> bool:
    stored_password, salt = stored_password.split(':')
    hashed_password = _encrypt_password(password.encode(),
                                        salt=bytes.fromhex(salt))
    return compare_digest(hashed_password, bytes.fromhex(stored_password))
