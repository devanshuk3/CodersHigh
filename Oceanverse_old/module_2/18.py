n = int(input("Enter the number of terms: "))
first = 0
second = 1

for i in range(n):
    print(first)
    next=first+second
    first=second
    second=next


# def function(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1 
#     else:
#         return function(n - 1) + function(n - 2)
# print(function(n))