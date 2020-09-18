from string import maketrans

def convert(s):
    mapped = maketrans("qwertyuiopasdfghjklzxcvbnm", "abcdefghijklmnopqrstuvwxyz")
    return s.translate(mapped)

s = "utta"
print convert(s)