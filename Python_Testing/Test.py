def isAnagram(str1, str2):
  if len(str1) != len(str2):
    return False

  dict = {}

  for i in range(len(str1)):
    if(str1 in dict):
      dict[str1[i]] += 1
    else:
      dict[str1[i]] = 1

  if(str2 not in dict):
    return False
  return True


str1 = 'llisten'
str2 = 'sillent'

print(isAnagram(str1, str2))