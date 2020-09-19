from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyz"
def convert(s, characterSet):
    mapped = maketrans(characterSet, alphabet)
    return s.translate(mapped)

def convertUsingZip(s, characterSet):
    a = dict(zip(characterSet, alphabet))
    s = [a[i] for i in s]
    return "".join(s)

newCharacterSet = "qwertyuiopasdfghjklzxcvbnm"
s = "utta"
print convert(s, newCharacterSet)
print convertUsingZip(s, newCharacterSet)