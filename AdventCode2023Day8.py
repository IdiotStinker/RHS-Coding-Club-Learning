pattern = "LRLRLRLLRRLRRLRRRLRRLRLLRRRLRRRLRRLLLLRRRLRLLRRLRRLRRLLLRRRLRRRLRRLRLRRLRLRLRLLRRRLRRRLLRRRLRRRLRRRLRLLLRRLRLRRRLRLRRRLLRRRLRLLRLRRRLRLRRRLRRLLRLRLRRLRLRLRRLRLRLRRRLRRLRLLRRLRRRLRRRLRRLRRRLRRLRLRRRLLRRRLLRRLRLRRRLRRRLLRRRLRLRRLRLRLRRLRLLRRLRLRLRRLRRRLRRRLRLRRLRRLLLRRRLLRLRRRLLRRRR"
with open("Year2023Day8.txt", "r") as file:
    a = file.read()



b = a.split("\n")

diction = {}

current = "AAA"
currentList = []
i = 0
times = 0
aCount = 0
aDict = []
correctList = []
for stuff in b:
    diction[stuff[0:3]] = stuff[7:15].split(", ")
    if stuff[2] == "A":
        aCount+=1
        currentList.append(stuff[0:3])
        correctList.append(False)
maybe = False
while not maybe:
    for j, dictCurrent in enumerate(currentList):
        if pattern[i] == "L":
            currentList[j] = diction[dictCurrent][0]
        elif pattern[i] == "R":
            currentList[j] = diction[dictCurrent][1]
    
    i+=1 
    if len(pattern) == i:
        i = 0 
    
    times+=1
    
    for index, cool in enumerate(currentList):
        if cool[2] == "Z":
            correctList[index] = True
        else:
            correctList[index] = False

print(times)