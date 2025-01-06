def searchList(myList, key):
    for i in range(0, len(myList)):
        if myList[i] == key:
            return i
    return -1

data = [50, 40, 0, -435, 23]
print(f"\nThe list is {data}")
searchElement = int(input("\nEnter search element: "))
res = searchList(data, searchElement)
print(f"\nSearch Element found at index {res}") if res != -1 else print("\nSearch Element is not in the List")