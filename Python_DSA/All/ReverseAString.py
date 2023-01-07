# Reverse a string by Two Ways

# Base

# Question - https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
# Solution - https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/

# By For Loop:

def reverse(s):
    str = ""
    for i in s:
        str = i + str
        
    return str
  
s = "Geeksforgeeks"
print(reverse(s))

# Using an extended slice

def reverse(string):
    string = string[::-1]
    return string
  
s = "Geeksforgeeks"
print(reverse(s))