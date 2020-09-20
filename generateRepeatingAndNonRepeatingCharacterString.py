def generate(s):
    p = set()
    rep = ""
    for i in s:
        if i in p:
            rep += i
            p.remove(i)
        else:
            p.add(i)
    return ("".join(p), rep)

a = "geeksforgeeks"
print generate(a)
