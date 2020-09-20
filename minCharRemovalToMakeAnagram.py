from collections import Counter

def minRemoval(s1, s2):
    d1 = Counter(s1)
    d2 = Counter(s2)
    onlys1 = d1 - d2
    onlys2 = d2 - d1
    common = onlys1 | onlys2
    list(common.elements())
    return len(list(common.elements()))

def minRemovalRaw(s1, s2):
    d1 = {}
    d2 = {}
    for i in s1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1
    for i in s2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1
    count = 0
    print d1, d2
    for key in d1.keys():
        if key in d2:
            count = count + max(d1[key], d2[key]) - min(d1[key], d2[key]) 
        else:
            count += d1[key]
    for key in d2.keys():
        if key not in d1:
            count += d2[key]
    return count

a = "abcddf"
b = "cbadef"
print minRemovalRaw(a, b)
