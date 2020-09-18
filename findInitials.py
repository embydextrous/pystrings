def findInitials(name):
    return " ".join([x[0].upper() for x in name.split()])

s = "Narendra Modardas Dodi"
print findInitials(s)