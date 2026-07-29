# a,b = 156,68
# count=0
# while a!=b:
#     if a>b:
#         a=a-b
#     else:
#         b=a-b
#     count+=1
# print(a)
# print(count)

#repeated subtraction approach 


#euclid's approach:
def gcd(a,b):
    count=0 
    while b!=0:
        a,b=b,a%b
        count+=1
    return a,count

maxCount = 0
indices = []

for i in range(10, 100):
    for j in range(10, 100):
        value, currCount = gcd(i, j)
        if currCount>maxCount:
            maxCount=currCount
            indices=[i, j]
print(maxCount, indices)

        





