data = "Run:1.7m/s, Chase:1.8m/s, Start:-2.1m, Length:10.0m, Flashlight:5.1m, Door:8.2m, Exit:10.1m"

def splitData():
    extraNewData = []
    thisAwesomeDictionary = {
        
    }
    newData = data.split(", ")
    for difData in newData:
        epic = difData.split(":")
        extraNewData.append(epic)

    
    print(extraNewData)



splitData()