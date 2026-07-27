import math

n = int(input("Enter the number:"))
l=[]
for i in range(1,n):
    l.append(math.pow(i,2))
print(l)