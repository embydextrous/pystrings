def initialsWithLastName(name):
    a = name.title().split()
    n = len(a)
    for i in range(n-1):
        a[i] = a[i][0]
    return ".".join(a)

a = "narendra modardas dodi"
print initialsWithLastName(a)
