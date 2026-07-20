a = int(input("Enter a:"))
d = int(input("Enter d:"))
b = int(input("Enter b:"))

for i in range(a, b+1):
    if (i-a)%d == 0:
        print(i)