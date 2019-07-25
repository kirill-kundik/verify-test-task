import hashlib


def calculate_hash(file_uri):
    with open(file_uri, 'rb') as in_file:
        return hashlib.sha256(in_file.read()).hexdigest()
