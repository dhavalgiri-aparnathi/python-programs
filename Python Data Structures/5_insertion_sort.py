def insertionSort(myList):
    for i in range(1, len(myList)):
        key = myList[i]
        j = i - 1
        while j >= 0 and key < myList[j]:
            myList[j+1] = myList[j]
            j = j - 1
        myList[j+1] = key

data = [50, 40, 30, 20, 10]
insertionSort(data)
print(data)