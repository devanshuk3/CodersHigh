import math
num = int(input("Enter the number:"))
def isPrime(num):
        if num<=1:
            isPrime = False
        else:
            isPrime = True
            for i in range(2, int(math.sqrt(num))+1):
                if num%i==0:    
                    isPrime = False
                    break
        return isPrime
                        
for i in range(2, num):
            if isPrime(i):
                print(i)