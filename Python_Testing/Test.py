

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