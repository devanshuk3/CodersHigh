num = int(input("Enter the number:"))
i = int(input("starting point:"))
j = int(input("ending point:"))
for i in range(i, j+1):
    result = num*i
    print(num, '*' ,i, '=' ,result)