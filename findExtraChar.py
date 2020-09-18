def findExtraChar(a, b):
    xor = 0
    for i in a:
        xor ^= ord(i)
    for i in b:
        xor ^= ord(i)
    return chr(xor)

a = "abcd"
b = "edcab"
print findExtraChar(a, b)