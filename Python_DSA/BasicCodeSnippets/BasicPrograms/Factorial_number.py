
# Python 3 program to find factorial of given number

# ======= METHOD 1 == Recursive approach: 

def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))

# ==== METHOD 2 == Iterative approach :

# Python 3 program to find 
# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# ==== METHOD 3 ==

# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))
 
 
 def factorial(n):
       
    res = 1
      
    for i in range(2, n+1):
        res *= i
    return res
 # Driver Code
num = 5;
print("Factorial of", num, "is",
factorial(num))


# ===== METHOD 4 == One line Solution (Using Ternary operator)

def factorial(n):
 
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
 
 
# Driver Code
num = 5
print ("Factorial of",num,"is",
      factorial(num))

# ====== METHOD 5 == By using In-built function : 

import math
 
def factorial(n):
    return(math.factorial(n))
 
 
# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))