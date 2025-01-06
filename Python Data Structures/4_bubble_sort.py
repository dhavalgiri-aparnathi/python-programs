def bubbleSort(myList):
    for i in range(0, len(myList)):
        for j in range (0, len(myList) - i - 1):
            if myList[j] > myList[j+1]:
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp

simpleList = [10, 0, -30, 12, 50]
print("\nThe list is :", simpleList)
bubbleSort(simpleList)
print("\nThe sorted list is :", simpleList)