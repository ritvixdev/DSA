# Python program to find the
# maximum of two numbers
 
 
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(maximum(a, b))

# ====== METHOD 2 == Using max() function
 
a = 2
b = 4
 
maximum = max(a, b)
print(maximum)

# ======== METHOD 3 == Using Ternary Operator

a = 2
b = 4
 
# Use of ternary operator
print(a if a >= b else b)

# ====== METHOD 4 == Using lambda function 

a=2;b=4
maximum = lambda a,b:a if a > b else b
print(f'{maximum(a,b)} is a maximum number')

# ===== METHOD 5 == Using list comprehension

a=2;b=4
x=[a if a>b else b]
print("maximum number is:",x)

