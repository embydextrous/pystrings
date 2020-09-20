from itertools import groupby

def removeAllConsecutiveDuplicates(s):
    result = ""
    for (key, group) in groupby(s):
        result += key
    return result

def removeAllConsecutiveDuplicatesRaw(s):
    result = s[0]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            result += s[i+1]
    return result

s = "aaaabbbb"
print removeAllConsecutiveDuplicates(s)