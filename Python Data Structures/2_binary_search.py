def binarySearch(myList, keyValue):
    low = 0
    mid = 0
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) // 2
        if myList[mid] > keyValue:
            high = mid - 1
        elif myList[mid] < keyValue:
            low = mid + 1
        else:
            return mid
    return -1

myList = [10, -20, 30, 40, 50]
print("\nList is:",myList)
myList.sort()
print("\nSorted List is:",myList)
searchElement = int(input("\nEnter search element: "))
result = binarySearch(myList, searchElement)
if result == -1:
    print(f"\nThe search element {searchElement} is not in the list")
else:
    print(f"\nThe search element {searchElement} found at index: {result}")