num = abs(int(input("enter the numbner:")))
prod =1

if num == 0:
        print("1")

elif num < 0:
        print("Invalid input!! The value should be >=0")
else:
        for i in range(num, 0, -1):
                prod*=i
        print(prod)