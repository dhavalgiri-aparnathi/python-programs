def linearSearch(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"The key {key} found at {i} index")
            return
    print(f"The key {key} is not in the list")

myList = [10, 20, 30, 40]
valueToSearch = int(input("Enter Search Key: "))
linearSearch(myList, valueToSearch)