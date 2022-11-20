
# find the todatl number of digits in a number

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print(f"The number of digits in the number are: {count}")

lst = [2,4,8,5,9,35,3,6,76,5,45,47,5,30]
n = 5

def occurance(lst, n):
    count  = 0
    for i in lst:
        if n == i:
            count += 1
    return count

print(f"elemrnt {n} occur {occurance(lst,n)} times")