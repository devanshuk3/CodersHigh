# 36. Write a function which simulates the process of throwing n
#  identical balls into n
#  bins. What is the maximum across the buckets? Write a short report on the output of your code. (2 points)
import random
num = int(input("Enter the number of balls and bins: "))
bins = [0]*num
for i in range(num):
    bin_num = random.randint(1,num)
    bins[bin_num - 1] += 1
print("The maximum number of balls are in:", max(bins))
print("the maximum number of balls in max bin is:",bins[max(bins)])