import hashlib

def to_md5(s):
    m = hashlib.md5()
    m.update(str(s).encode('utf-8'))
    result = m.hexdigest()
    return result