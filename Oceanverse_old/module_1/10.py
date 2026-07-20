import math
num = int(input("Enter the number:"))

if num<=1:
    print("Not Prime")
else:
    isPrime = True
    for i in range(2, int(math.sqrt(num))):
        if num%i==0:    
            isPrime = False
            break
    if isPrime:
        print("Prime")
    else :
        print("Not prime")