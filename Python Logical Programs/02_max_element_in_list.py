def getMaximumElement(myList):
    max = myList[0]
    for i in range(0, len(myList)):
        if myList[i] > max:
            max = myList[i]
    print("\nMaximum element is:", max)

data = [45, 43, -45, 65, 999, 233]
getMaximumElement(data)