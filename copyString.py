def copyString(s1, s2):
    for i in s1:
        s2 += i

s1 = "Narednra Damodardas Bhai Modi"
s2 = []
copyString(s1, s2)
print "".join(s2)
