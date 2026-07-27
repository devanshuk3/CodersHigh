string = input("Enter the string: ")
stringList = list(string)
i=0
j=len(string)
tempList = ['']
print(tempList)
while(i<j):
    tempList[0] = stringList[i]
    stringList[i] = stringList[j-1]
    stringList[j-1] = tempList[0]
    i+=1
    j-=1
    # print(tempList)
print("".join(stringList)) 

