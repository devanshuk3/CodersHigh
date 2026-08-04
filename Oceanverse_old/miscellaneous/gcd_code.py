a,b = 156,68
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
    while b!=0:
        count=0 
        a,b=b,a%b
        count+=1
    return a,count
ai, count = gcd(a,b)
maxCount = 0
indices = []
# print(ai)
# print(count)
for i in range(10,99):
     for j in range(10,99):
        ai, count = gcd(i,j)
        if count > maxCount:
            maxCount = count
            indices = [i,j]
print(maxCount)
print(indices)