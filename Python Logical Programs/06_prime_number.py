def isPrimeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return -1
    return 1

res = isPrimeNumber(7)
print("Prime Number") if res == 1 else print("Not Prime Number")