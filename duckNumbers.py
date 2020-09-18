def isDuckNumber(s):
    s = s.lstrip('0')
    for i in s:
        if i == '0':
            return True
    return False

n = "1023"
print isDuckNumber(n)
n = "0012"
print isDuckNumber(n)
n = "0"
print isDuckNumber(n)
n = "0102"
print isDuckNumber(n)