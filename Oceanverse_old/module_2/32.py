import random
n = int(input("Enter the number of elements: "))
list = []
for i in range(n):
    list.append(random.randint(1,1000))
print(list)