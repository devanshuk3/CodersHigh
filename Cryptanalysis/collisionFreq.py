sentence1 = "The morning sun spread a warm golden light across the quiet park as birds sang from the tall trees. A gentle breeze carried the scent of fresh flowers, making the air feel calm and refreshing. Children laughed while playing on the swings, and a few people enjoyed jogging along the winding paths. An elderly man sat on a wooden bench reading a newspaper, occasionally looking up to admire the peaceful surroundings. Nearby, a small fountain sparkled in 1the sunlight, attracting curious pigeons. It was the kind of morning that inspired people to slow down, appreciate nature, and begin the day with positivity."
sentence2 = "Technology has become an essential part of modern life, influencing the way people communicate, learn, and solve problems. Smartphones, computers, and the internet have made information available within seconds, helping students and professionals work more efficiently. Online learning platforms provide access to quality education from anywhere in the world, while digital tools simplify everyday tasks such as shopping, banking, and health1care. However, balancing screen time with outdoor activities and personal interactions is equally important. By using technology responsibly and thoughtfully, individuals can enjoy its many benefits while maintaining healthy relationships, creativity, and overall well-being."

before1 = ""
before2 = ""
for i in range(len(sentence1)):
    if sentence1[i].isalpha():
        before1 += sentence1[i].lower()
# print(before1)
for i in range(len(sentence2)):
    if sentence2[i].isalpha():
        before2 += sentence2[i].lower()
# print(before2)
length = min(len(before1), len(before2))
beforeFreq = 0
beforeCount = {}

for i in range(length):
    if before1[i] == before2[i]:
        beforeFreq += 1
        beforeCount[before1[i]] = beforeCount.get(before1[i], 0) + 1

beforeCollision = beforeFreq / length
maxVal = 0
va1 = 0
val2 =  0
for j in range(26):
    for k in range(26):
        string1 = ""
        string2 = ""
        for i in range(len(sentence1)):
            if sentence1[i].isalpha():
                ch = chr((ord(sentence1[i].lower()) - ord('a') + j) % 26 + ord('a'))
                string1 += ch
                
        for i in range(len(sentence2)):
            if sentence2[i].isalpha():
                ch = chr((ord(sentence2[i].lower()) - ord('a') + k) % 26 + ord('a'))
                string2 += ch

        length = min(len(string1), len(string2))

        afterFreq = 0
        afterCount = {}

        for i in range(length):
            if string1[i] == string2[i]:
                afterFreq += 1
                afterCount[string1[i]] = afterCount.get(string1[i], 0) + 1
                afterCollision = afterFreq / length
                if afterCollision > maxVal:
                    val1 = j
                    val2 = k
                    maxVal = afterCollision
                #the maximum value is attained at the point where there is no shift!!
                print("collision frequency after shift:",j, k, afterCollision)

print("Maximum value:",maxVal)
print(val1, val2)
# afterCollision = afterFreq / length
# print("collision before shift:",beforeFreq)
print("collision frequency before shift:",beforeCollision)
# print("collision after shift:", afterFreq)
# print("collision frequency after shift:",afterCollision)
# overallChange=((afterCollision-beforeCollision)/beforeCollision)*100
# print("Overall percentage Change :", round(overallChange, 2),"%")
# print("\nCharacter-wise Collision Changes:\n")
# letters = sorted(set(beforeCount.keys())|set(afterCount.keys()))
# #sort the keys(acc to alphabetic order) and store them in a set(this removes all the duplicate values.)
# #the union operator "|" combines two sets
# for ch in letters:
#     before = beforeCount.get(ch, 0)
#     after = afterCount.get(ch, 0)
#     print(ch)
#     print("before:",before)
#     print("after:",after)
#     if before == 0:
#         print("percentage change:new collision")
#     else:
#         percent=((after-before)/before)*100
#         print("Percentage change:",round(percent,2),"%")
#     print()