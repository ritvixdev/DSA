# find number of numbers that has even number of digits.

def findNumbers(nums):
    count = 0
    for i in nums:
        if even(i):
            count += 1
            
    return count


def even(num):
    numberOfDigits = digits(num)
    if numberOfDigits % 2 == 0:
        return True
    return False
        
        
def digits(num):
    count = 0 
    
    while num > 0:
        count = count +1
        num /= 10
    
    return count

    
        
nums = [12,345,2,6,7896]
print(findNumbers(nums))