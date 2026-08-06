num = int(input("Enter the number:"))
res = ""
while num!=0:
    rem = num % 2
    res += str(rem)
    num = num//2
res = res[::-1]
print(res)