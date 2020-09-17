# Strings are 0-indexed like arrays
a = "geeks for geeks"
print a[3] # prints k
print a[-2] # prints k, reverse index is from -1

# Slicing s[begin:end:step]

print a[2:5] # prints eks, end index not included
print a[2:] # prints 'eks for geeks' if end index is not mentioned; prints fron begin index to end of string
print a[:5] # prints geeks, print all before endIndex if beginIndex is not mentioned
print a[-5:-3] # prints `ge`
print a[4:2:-1] # prints `sk`
print a[::-1] # reverses string

str1 = "geeksforgeeks is for geeks"
str2 = "geeks"
print len(str1) # prints length of string
print str1.find(str2, 4) # prints next starting index in str1[4:]
print str1.find("234") # prints -1 if not found

print str1.rfind(str2, 4) # prints last starting index in str1[4:]
print str1.startswith("geeks") # True if str1 starts with passed String
print str1.endswith("geeks") # True if str1 ends with passed String

print str1.isupper() # True if string is in upper case
print str1.islower() # True if string is in lower case
print str1.upper() # New upper case string
print str1.lower() # New Lower case String
print str1.title() # New Title Case String
print str1.swapcase() # New string with case changed from upper to lower and vice versa
print str1.capitalize() # Capitalized first letter
print str1.center(41, "-") # Makes total length of new string to 41 by appending and prepending `-` with str1 centered. Extra `-` is inserted on LHS.
print str1.ljust(30, "-") # appends 30 - len(str1) `-`
print str1.rjust(30, "-") # prepends 30 - len(str1) `-`

print str1.count('e', 5, 21) # counts number of occurences of `e` between index 5 and 20
print str1.count('geeks') # prints 3 scans full string

s1 = "123"
s2 = "a2"
s3 = "geeks"
s4 = "   \t"

print s1.isalnum() # If contains alphabets and numbers
print s4.isalnum() # false
print s3.isalpha() # All are alphabets
print s2.isalpha() # false
print s1.isalpha() # false
print s1.isdigit() # All are digits
print s2.isdigit() # False
print s4.isspace() # True is string contains only whitespace characters
print s1.isspace() # false

a = ["geeks", "for", "geeks"]
p = "_"
print p.join(a) # prints strings from array joined by p (`_`)

str1 = "---sdda--dff----"
print str1.strip("-") # Removes all trailing and leading `-`
print str1.rstrip("-") # Removes all leading `-`
print str1.lstrip("-") # Removes all trailing `-`

print min("geeks") # Returns minimum char `e` 
print max("geeks") # returns maximum char `s`
print min('Aa') # Ascii based prints 'A'

from string import maketrans

str1 = "geek"
str2 = "pqrs"
mapped = maketrans(str1, str2) # make trans creates mapping for each character in str1 to str2
s = "geeksforgeeks"
print s.translate(mapped) # translate replaces each character of s in str1 with its mapping from str2

print s.replace("e", "_", 3) # Replaces first 3 `e` with `_`
print s.replace("geeks", "moddu") # Prints modduformoddu

s = "Arjit\tis\tpoo\tpoo."
print s
print s.expandtabs(8) # expands tabs to specified number of spaces

print s.zfill(20) # prepends with 0 to make string of size 20

s = "this\n is a new\n split"
print s.splitlines() # Splits based on newline character
s = "geeks for geeks"
print s.split() # Splits based on space
s = "geeks-for-geeks"
print s.split("-") # Splits based on "-"