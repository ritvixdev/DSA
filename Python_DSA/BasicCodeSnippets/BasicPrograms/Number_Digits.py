
# find the todatl number of digits in a number

# n=int(input("Enter number:"))
# count=0
# while(n>0):
#     count=count+1
#     n=n//10
# print(f"The number of digits in the number are: {count}")

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range (len(x)):
    for j in range (len(y)):
        result[i][j] = x[i][j] + y[i][j]
        
for r in result:
    print(r)