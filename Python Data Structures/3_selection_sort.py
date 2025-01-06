def ascendingSelectionSort(arr):
    for i in range(len(arr)):
        for j in range((i + 1), len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

def descendingSelectionSort(arr):
    for i in range(len(arr)):
        for j in range((i + 1), len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

myList = [50, 40, 30, 20, 10]
ascendingSelectionSort(myList)
descendingSelectionSort(myList)