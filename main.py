def divingBoard(shortLength, longLength, count):
    returnList = []
    totalCount = count + 1
    for a in range(totalCount):
        returnList.append(shortLength*a + longLength*(count-a))
    return returnList

# lengths = []
# shortLength = 1
# longLength = 2
# count = 3
# for a in range(count+1):
#     lengths.append(shortLength*a + longLength*(count-a))


# print(lengths)


