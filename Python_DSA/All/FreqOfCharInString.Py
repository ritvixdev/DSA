#  Frequency of each character in String

# Basics

# Question - https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
# Solution - https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

# By For in

def checkFreq(str):
  freq = {}
  
  for i in str:
    if i in freq:
      freq[i] += 1
    else:
      freq[i] = 1

  return freq
 
str = "GeeksforGeeks"
print(checkFreq(str))

# By dict.get()

# dict.get()
 
test_str = "GeeksforGeeks"
 
res = {}
 
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
 
print("Count of all characters in GeeksforGeeks is : \n"
      + str(res))

