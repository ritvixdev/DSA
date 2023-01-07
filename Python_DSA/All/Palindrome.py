# Python program to check if a string is palindrome or not

# Basic

# Question - https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/
# Solution - https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/


#  By for loop

def isPalindrome(str):
  
  length = len(str)
  mid = length//2

  for i in range(0, mid):
    if str[i] != str[length -1 -i]:
      return False
  return True
 
str = "malayalam"
print(isPalindrome(str))

# Using an extended slice

def isPalindrome(s):
    return s == s[::-1]
 
s = "malayalam"
print(isPalindrome(s))