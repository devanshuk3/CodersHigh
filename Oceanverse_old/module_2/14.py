str1 = input("Enter the string:")
i=len(str1)-1
str2=""
for j in range(i, -1,-1):
    str2+=str1[j]
    j-=1
print(str2)