import hashlib

file = open("rockyou-20.txt")
y = file.read()

for x in y.split('\n'):
    x = x.encode()
    HashedText = "secret"
    if hashlib.md5(x).hexdigest() == HashedText:
        x = (x.decode())
        exit()

    HashedText = "secret"
    if hashlib.sha256(x).hexdigest() == HashedText:
        x = (x.decode())
        exit()

    HashedText = "secret"
    if hashlib.sha512(x).hexdigest() == HashedText:
        x = (x.decode())
        exit()

print()