import hashlib


def get_md5(num):
    md5 = hashlib.md5()
    md5.update(num.encode('utf-8'))
    return md5.hexdigest()


