# zk_login.py
import hashlib
import random

def generate_challenge():
    return str(random.randint(100000, 999999))

def prove(secret, challenge):
    return hashlib.sha256((secret + challenge).encode()).hexdigest()

def verify(response, secret, challenge):
    expected = prove(secret, challenge)
    return response == expected
