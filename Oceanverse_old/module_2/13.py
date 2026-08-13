str1 = input("Enter the first string:")
str2 = input("Enter the second string:")
str3 =""
length = max(len(str1), len(str2))
i=0
while i<length:
    if(i<len(str1)):
        str3+=str1[i]
    if(i<len(str2)):
        str3+=str2[i]
    i+=1
print(str3) 