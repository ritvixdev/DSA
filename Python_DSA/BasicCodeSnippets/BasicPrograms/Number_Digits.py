
# find the todatl number of digits in a number

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print(f"The number of digits in the number are: {count}")

lst = [2,4,8,5,9,35,3,6,76,45,47,30]

lst2 = []
for i in lst:
    if i % 2 == 0:
        print(i, end=" ")