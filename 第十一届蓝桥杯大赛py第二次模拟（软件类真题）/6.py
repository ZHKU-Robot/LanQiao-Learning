origin = "lanqiao"

def encrypt(originstr):
    return ''.join([chr(ord(s) + 3) for s in list(originstr)])

print(encrypt(origin))
