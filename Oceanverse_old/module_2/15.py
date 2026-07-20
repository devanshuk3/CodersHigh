str1 = input("Enter the string:")
i=len(str1)-1
str2=""
for j in range(i, -1,-1):
    str2+=str1[j]
    j-=1
if str1 == str2:
    print("String is a palindrome!!")
else:
    print("String is not a palindrome!!")