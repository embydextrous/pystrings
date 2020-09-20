def mirror(s):
    result = ""
    for i in s:
        asc = ord(i)
        if (asc >= ord('A') and asc <= ord('Z')):
            length = ord('Z') - ord('A') + 1
            key = ord('Z') - (asc - ord('A'))
            result += chr(key)
        elif (asc >= ord('a') and asc <= ord('z')):
            length = ord('z') - ord('a') + 1
            key = ord('z') - (asc - ord('a'))
            result += chr(key)        
        else:
            result += i
    return result

s = "Geeks for geeks is + fuck MODI"
print mirror(s)