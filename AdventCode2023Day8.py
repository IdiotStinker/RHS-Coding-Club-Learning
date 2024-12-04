pattern = "LRLRLRLLRRLRRLRRRLRRLRLLRRRLRRRLRRLLLLRRRLRLLRRLRRLRRLLLRRRLRRRLRRLRLRRLRLRLRLLRRRLRRRLLRRRLRRRLRRRLRLLLRRLRLRRRLRLRRRLLRRRLRLLRLRRRLRLRRRLRRLLRLRLRRLRLRLRRLRLRLRRRLRRLRLLRRLRRRLRRRLRRLRRRLRRLRLRRRLLRRRLLRRLRLRRRLRRRLLRRRLRLRRLRLRLRRLRLLRRLRLRLRRLRRRLRRRLRLRRLRRLLLRRRLLRLRRRLLRRRR"
with open("Year2023Day8.txt", "r") as file:
    a = file.read()



b = a.split("\n")

diction = {}

current = "AAA"
currentList = []
i = 0
times = 0
aDict = []
correctList = []
endLoop = False
for stuff in b:
    diction[stuff[0:3]] = stuff[7:15].split(", ")
    if stuff[2] == "A":
        print(stuff[0:3])
        currentList.append(stuff[0:3])
        correctList.append(False)


while not endLoop:

    for j, item in enumerate(currentList):
        if pattern[i] == "L":
            currentList[j] = diction[item][0]
        elif pattern[i] == "R":
            currentList[j] = diction[item][1]
        else:
            print("error")
    
    i+=1 
    if len(pattern) == i:
        i = 0 
    
    times+=1
    
    for k, cool in enumerate(currentList):
        if cool[2] == "Z":
            correctList[k] = True
        else:
            correctList[k] = False

    for bool in correctList:
        if bool != True:
            endLoop = False
            break
        else:
            endLoop = True

    
    

print(times)