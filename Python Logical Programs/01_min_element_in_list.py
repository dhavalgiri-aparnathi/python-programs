def getMinumumElement(myList):
    min = myList[0]
    for i in range(0, len(myList)):
        if myList[i] < min:
            min = myList[i]
    print("\nMinimum element is:", min)

data = [100,-20,30,40,50]
getMinumumElement(data)