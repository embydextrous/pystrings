def checkIfInteger(s):
    if len(s) == 0:
        return False
    for i in s:
        if ord(i) < ord('0') or ord(i) > ord('9'):
            return False
    return True

a = "124"
b = "23b"
c = "23.7"
d = "sam"
print checkIfInteger(a)
print checkIfInteger(b)
print checkIfInteger(c)
print checkIfInteger(d)

