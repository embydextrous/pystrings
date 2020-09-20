from collections import Counter

def checkAnagram(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    d = d1 - d2
    return len(d1-d2) == 0

def checkAnagramRaw(s1, s2):
    d = {}
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s2:
        if i in d:
            d[i] -= 1
            if d[i] == 0:
                d.pop(i)
    return len(d) == 0

a = "geeks"
b = "geeks"
print checkAnagram(a, b)
print checkAnagramRaw(a, b)