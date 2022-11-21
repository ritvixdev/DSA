
# find the todatl number of digits in a number

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print(f"The number of digits in the number are: {count}")

lst = [2,4,8,5,9,35,3,6,76,5,45,47,5,30]

n = int(len(lst))
sum1  = 0
lst2 = []

for i in range(n):
    sum1 += lst[i]
    lst2.append(sum1)
    
print(lst2)