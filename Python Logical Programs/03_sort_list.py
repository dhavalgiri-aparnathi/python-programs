def sortList(myList):
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList) - 1):
            if myList[i] > myList[j]:
                myList[i], myList[j] = myList[j], myList[i]

data = [-34, 45, 65, 0, 76]
print("\nUnsorted List:", data)
sortList(data)
print("\nSorted List:", data)