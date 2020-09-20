def maxLengthOf1InBinaryString(s):
    a = s.split("0")
    return max(map(len, a))

s = "101110101011110110110101010101000"
print maxLengthOf1InBinaryString(s)