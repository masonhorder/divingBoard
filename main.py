def divingBoard(shortLength, longLength, count):
    returnList = []
    for a in range(totalCount+1):
        returnList.append(shortLength*a + longLength*(count-a))
    return returnList

print(divingBoard(1,2,3))


