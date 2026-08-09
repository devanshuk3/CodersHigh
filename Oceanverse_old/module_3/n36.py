import random
num = int(input("Enter the number of balls and bins: "))
bins = [0]*num #this initiates a list with value 0 for each bin
def throw_balls(num, bins):
    #throws one ball into a random bin for each ball
    for i in range(num):
        bin_num = random.randint(1,num)
        bins[bin_num-1] += 1

    max_balls=max(bins)#maximum balls in a bin
    max_bin=bins.index(max_balls)#index of that bin

    # print("balls in each bin:",bins)
    # print("the bin with the maximum balls is:",max_bin+1)
    # print("the maximum number of balls in a bin is:",max_balls)

    nonEmptyBins = 0
    for i in range(len(bins)):
        if bins[i] == 0:
            nonEmptyBins+=1
    print("the number of non-empty bins is:", nonEmptyBins)

throw_balls(num, bins)