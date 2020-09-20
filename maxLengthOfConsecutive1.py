def maxLengthOf1InBinaryString(s):
    a = s.split("0")
    return max(map(len, a))

def maxLengthOf1InBinaryStringRaw(s):
    maxLength = 0
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
        else:
            if count > maxLength:
                maxLength = count
            count = 0
    return maxLength

s = "101110101011110110110101010101000"
print maxLengthOf1InBinaryStringRaw(s)