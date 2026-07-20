n = int(input("Enter the number:"))
sum =0
# for i in range(n):
#     sum+=i
#     print(sum)
i=0
while (i<=n):
    sum+=i
    i+=1
print(sum)

print(sum(range(n+1)))