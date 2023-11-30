import hashlib


def Covert_to_HASH(password):
    password = "a1s2d3"+password + "j7k8l9"
    hash_object = hashlib.sha256()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password

#just checking