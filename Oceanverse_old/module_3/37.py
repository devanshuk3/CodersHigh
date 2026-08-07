import random
num = int(input("Enter the number of bins: "))
bins=[0]*num
balls_thrown=0
while 0 in bins:
    bin_num = random.randint(1,num)
    bins[bin_num-1]+=1
    balls_thrown+=1
print("balls thrown til the bins are non empty is:",balls_thrown)