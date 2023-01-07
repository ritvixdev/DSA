# Check if a string can be obtained by rotating another string 2 places


# Asked in Company - Infosys

# Question - https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/
# Solution - https://www.geeksforgeeks.org/check-string-can-obtained-rotating-another-string-2-places/

def isRotating(str1, str2):
  if(len(str1) != len(str2)):
    return False

  if(len(str1) < 2):
    return str1 == str2

  clock_rot = ""
  anticlock_rot = ""
  
  l = len(str2)

  anticlock_rot = (anticlock_rot + str2[l-2:] + str2[0: l-2])

  clock_rot = (clock_rot + str2[2:] + str2[0:2])

  return (str1 == clock_rot or str1 == anticlock_rot)



if __name__ == "__main__":
  str1 = "geeks"
  str2 = "eksge"

if isRotating(str1, str2):
  print("yes")
else:
  print("No")
