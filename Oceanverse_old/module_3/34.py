num = int(input("enter the numbner:"))
def factorial(num):
        prod =1
        for i in range(num, 1, -1):
                prod*=i
        return prod


print(factorial(num))