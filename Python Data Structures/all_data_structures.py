def linearSearch(arr, key):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == key:
            return i
    return -1

def binarySearch(arr, key):
    n = len(arr)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        index = i
        for j in range(i+1, n):
            if arr[index] > arr[j]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

def bubbleSort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    n  = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [50, 40, 30, 20, 10]
print(arr)
# Call needed functions