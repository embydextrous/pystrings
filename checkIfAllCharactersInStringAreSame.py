def checkIfAllCharsAreSame(s):
    for i in s:
        if i != s[0]:
            return False
    return True

s = "gggg"
print checkIfAllCharsAreSame(s)
s = "ffff2"
print checkIfAllCharsAreSame(s)
s = "2ffff"
print checkIfAllCharsAreSame(s)