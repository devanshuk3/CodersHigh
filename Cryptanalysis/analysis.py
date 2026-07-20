from collections import Counter
#counter is used to sort the letters on the basis of frequencies -- outputs a dictionary -- key: letter and value: letter
freqCount = {}
#empty dict
with open("encrypted.txt", "r") as f:
    #countList = [0 for i in range(26)] empty array for char freq
    word = f.readline() #gets lines from the file
    #readlines -- can give range
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    while(word):
        for i in word:
            if(i == "\n"):
               continue
            freqCount[i] = freqCount.get(i, 0)+1
        word = f.readline() #this is used for traversal
print(freqCount)

#countList.sort(reverse = True)
#print(countList)
#test = "mfttdmfttdmfttdmfttdmfttd"
#x = Counter(test)
#sortedTest = sorted(x.items(), key = lambda item: item[1], reverse = True)
def get_count(item):
    return item[1] #this is the value in dictionary
#sort function == mutates the original list
#sorted = stores it in a different variable(does not change original)

#sortedFreq = sorted(freqCount.items(), key = get_count, reverse = True)

items = list(freqCount.items())

for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[j][1]>items[i][1]:
            items[i],items[j] = items[j],items[i]
#reverse true -- descending and reverse false -- gives ascending order
letters = ['E', 'A', 'R', 'I', 'O', 'T', 'N', 'S', 'L', 'C', 
    'U', 'D', 'P', 'M', 'H', 'G', 'B', 'F', 'Y', 'W', 
    'K', 'V', 'X', 'Z', 'Q', 'J']
#dictionary === hashmap
dictionary = {}
#for i, (let, cnt) in enumerate(sortedFreq):
   # dictionary[let] = letters[i]
#print(dictionary)

#i = 0
#for let,cnt in sortedFreq:
#    dictionary[let] = letters[i]
#    i+=1
#print(dictionary)

for i in range(len(items)):
    letter = items[i][0]
    dictionary[letter] = letters[i]
print(dictionary)
f.close()

with open("encrypted.txt", "r") as f, open("decrypted.txt", "w") as d:
    for line in f:
        newLine = ""
        for char in line:
            if(char == "\n"):
                continue
            newLine += dictionary[char].lower()
        d.write(newLine + '\n')
f.close()
d.close()
