num = int(input("Enter the size of the start pattern: "))

for i in range(1, num+1):
    for j in range(i):
        print("*", end="")
    print()

# the print function has a parameter called end. By default it is set to end="\n"
#here, we are modifying it to not change the line after every iteration.
#becayse it is set to an empty string, it appends the next output just after the current one.
