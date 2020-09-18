def isPangramaticLipogram(s):
    s = s.lower()
    a = set()
    for i in range(ord('a'), ord('z') + 1):
        a.add(chr(i))
    for i in s:
        if i in a:
            a.remove(i)
    print len(a)
    return len(a) == 1

s1 = "The quick brown fox jumped over the lazy dog"
s2 = "The quick brown fox jumps over the lazy dog"
s3 = "The quick brown fox jum over the lazy dog"

print isPangramaticLipogram(s1)
print isPangramaticLipogram(s2)
print isPangramaticLipogram(s3)