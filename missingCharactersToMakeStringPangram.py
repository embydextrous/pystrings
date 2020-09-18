def missingCharacters(s):
    a = [False] * 26
    s = s.lower()
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            a[ord(i) - ord('a')] = True
    result = []
    for i in range(26):
        if not a[i]:
            result.append(chr(i + ord('a')))
    return "".join(result)

s = "welcome to geeksforgeeks"
print missingCharacters(s)