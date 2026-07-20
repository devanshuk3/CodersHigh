String1 = input("Enter the string: ")
vowelsCount =0
consonantsCount =0
length = len(String1)
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(length):
    if String1[i] in vowels:
        vowelsCount+=1
    else:
        consonantsCount +=1
print('Vowels:' ,vowelsCount)
print('Consonants:', consonantsCount)