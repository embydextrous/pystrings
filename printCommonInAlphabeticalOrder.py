from collections import Counter

def findCommon(s1, s2):
    d = {}
    result = []
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s2:
        if c in d:
            result.append(c)
            d[c] -= 1
            if d[c] == 0:
                d.pop(c)
    return "".join(sorted(result))

def findCommon2(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    d = d1 & d2
    return "".join(sorted(list(d.elements())))

s1 = "forgeeks"
s2 = "wikileeks"
print findCommon(s1, s2)
print findCommon2(s1, s2)
