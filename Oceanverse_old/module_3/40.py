i=0
count = 1

#right = (i+count, j)
#up = (i, j+count)
#count+=1
#left = (i-count, j)
#down = (i, j-count)
n = int(input("Enter the required length of the string:"))
result = ""
for i in range(n):
    if i%2 != 0:
        #instead of calculating the indices, we set the logic for pattern related to even and odd parameters
        result += (i*'R' + i*'U')
    else:
        result += (i*'L'+ i*'D')
print(result[:n])