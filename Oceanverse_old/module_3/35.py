n = int(input("Enter the number: ")) 
# k=0
# for i in range(n):
#     k+=i
#     print(k)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n))