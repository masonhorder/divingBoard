def divingBoard(longLength, shortLength, count):
    returnList = []
    totalCount = count + 1
    
    for a in range(totalCount):
        miniList = []
        longCount = 0
        while longCount < a:
            miniList.append(longLength)
            longCount += 1
        shortCount = 0
        while shortCount < count-longCount:
            miniList.append(shortLength)
            shortCount += 1
        print(miniList)
        returnList.append(sum(miniList))
        
    
    print("----------")
    return returnList

print(divingBoard(77,93,100))


