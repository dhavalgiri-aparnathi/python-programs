def printFibonacciSeries(n):
    n1 = 0
    n2 = 1
    for i in range(0, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3

printFibonacciSeries(10)