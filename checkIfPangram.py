def isPangram(s):
    a = set()
    s = s.lower()
    for i in range(26):
        a.add(chr(97 + i))
    for i in s:
        if i in a:
            a.remove(i)         
    return len(a) == 0

s = "Narendra Damodardas Modi"
print isPangram(s)
s = "The quick brown fox jumps over the little lazy dog"
print isPangram(s)