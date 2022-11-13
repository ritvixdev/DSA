def linearSearch(str, target):
    
    for i in range(len(str)):
        if str[i] == target:
            return i
    return -1
 
str = 'spring is the best time to plant blueberry'
 
target = 'e'
ans = linearSearch(str, target)
 
if ans >= 0:
    print(f"{target} is found at index {ans}")
else :
    print(f"{target} was not found")



# ============== Search for string index=================

#====method2=======
#== find ()

# word = 'who knows how to write perfect code'
 
# # returns first occurrence of Substring
# result = word.find('knows')
# print("Substring 'knows' found at index:", result)
 
# result = word.find('to')
# print("Substring 'to ' found at index:", result)
 
# # How to use find()
# if word.find('haha') != -1:
#     print("Contains given substring ")
# else:
#     print("Doesn't contains given substring")



#==== Method 3==========
# word = 'who knows how to write perfect code'
 
# # Substring is searched in 'kn for knows'
# print(word.find('kn', 2))
 
# # Substring is searched in 'eks for geeks'
# print(word.find('knows', 2))
 
# # Substring is searched in 's for h'
# print(word.find('h', 9, 13))
 
# # Substring is searched in 's for to'
# print(word.find('to ', 13, 20))