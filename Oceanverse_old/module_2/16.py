String1 = input("Enter the string: ")

vowelsCount = 0

consonantsCount = 0
numbersCount = 0
specialCount = 0
lowerVowels = ['a', 'e', 'i', 'o', 'u']
upperVowels = ['A', 'E', 'I', 'O', 'U']

lowerConsonants = ['b','c','d','f','g','h','j','k','l','m','n', 'p','q','r','s', 't','v','w','x','y','z']
upperConsonants = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

specialCharacters = ['!','@','#','$','%'," ^"]
for ch in String1:

    if ch in lowerVowels:
        vowelsCount+=1

    elif ch in upperVowels:
        vowelsCount+=1

    elif ch in lowerConsonants:
        consonantsCount+=1

    elif ch in upperConsonants:
        consonantsCount+=1

    elif ch in numbers:
        numbersCount+=1

    elif ch in specialCharacters:
        specialCount+=1

print("Vowels =",vowelsCount)
print("Consonants =",consonantsCount)
print("Numbers =",numbersCount)
print("Special Characters =",specialCount)