import random
import linecache
freqCount = {}
#empty dict
with open("words2.txt", "r") as f:
    word = f.readline()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    while(word):
        for i in word:
            if(i == "\n"):
               continue
            freqCount[i] = freqCount.get(i, 0)+1
        word = f.readline() 
print(freqCount)



freqCount2 = {}
for i in range(1000):
     b = random.randint(1, 370105)
     word2 = linecache.getline('words.txt', b)
     for i in word2:
               if(i == "\n"):
                continue
               freqCount2[i] = freqCount2.get(i, 0)+1 
print(freqCount2)

freqCount3 = {}
for i in range(1000):
     a = random.randint(1, 370105)
     word2 = linecache.getline('words.txt', a)
     for i in word2:
               if(i == "\n"):
                continue
               freqCount3[i] = freqCount3.get(i, 0)+1 
print(freqCount3)