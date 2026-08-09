list = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    list.append(element)
print("The list is:", list)

maxValue = 0
for i in range(len(list)):
    maxValue = max(list[i], maxValue)
print("The maximum value in the list is:", maxValue)