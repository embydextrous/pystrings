def removePunctuations(s):
    p = '!"#$%&\'()*+,-./:;?@[\]^_`{|}~ '
    for i in p:
        s = s.replace(i, "")
    return s

s = "Welcome???@@##$ to#$ Geeks%$^for$%^&Geeks"
print removePunctuations(s)