thingy = ""
INPUT = "146443 156468 166438 176463   186898 196503   206423 216898 226449   236908 246453 256498 266903"
#INPUT = "171   1 20 34 91   51 93 71 218 18 131"
words = []
for word in INPUT.split("   "):
    curWord = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for numLetter in word.split():
        num = int(numLetter) -1#this is because we don't include 0
        exp = 1
        #print(num, (pow(10, exp)-(pow(10, exp-1))) * exp)
        while num > (pow(10, exp)-(pow(10, exp-1))) * exp:
            num -= (pow(10, exp)-(pow(10, exp-1))) * exp
            exp += 1
            #print(num, (pow(10, exp)-(pow(10, exp-1))) * exp)
        #print(str(pow(10, exp-1) + int(num/exp)) + str(pow(10, exp-1) + int(num/exp) + 1), num%exp)
        #print(alphabet[int((str(pow(10, exp-1) + int(num/exp)) + str(pow(10, exp-1) + int(num/exp) + 1))[num%exp: num%exp+2])-1])
        curWord += (alphabet[int((str(pow(10, exp-1) + int(num/exp)) + str(pow(10, exp-1) + int(num/exp) + 1))[num%exp: num%exp+2])-1])
    words.append(curWord)

print(" ".join(words))