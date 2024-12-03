pattern = "LRLRLRLLRRLRRLRRRLRRLRLLRRRLRRRLRRLLLLRRRLRLLRRLRRLRRLLLRRRLRRRLRRLRLRRLRLRLRLLRRRLRRRLLRRRLRRRLRRRLRLLLRRLRLRRRLRLRRRLLRRRLRLLRLRRRLRLRRRLRRLLRLRLRRLRLRLRRLRLRLRRRLRRLRLLRRLRRRLRRRLRRLRRRLRRLRLRRRLLRRRLLRRLRLRRRLRRRLLRRRLRLRRLRLRLRRLRLLRRLRLRLRRLRRRLRRRLRLRRLRRLLLRRRLLRLRRRLLRRRR"
with open("2023Day8.txt", "r") as file:
    a = file.read()

print(a)

b = a.split("\n")

print(b)

diction = {
    
}

current = "AAA"
i = 0
times = 0
aCount = 0
for stuff in b:
    diction[stuff[0:3]] = stuff[7:15].split(", ")
    if stuff[2] == "A":
        aCount+=1

print(diction)

while current != "ZZZ":
    if pattern[i] == "L":
        current = diction[current][0]
    else:
        current = diction[current][1]
    i+=1
    if len(pattern) == i:
        i = 0
    times+=1

print(times)