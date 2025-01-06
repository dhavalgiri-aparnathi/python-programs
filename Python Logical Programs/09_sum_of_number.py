def sumOfNumber(n):
    sum = 0
    while n != 0:
        remainder = n % 10
        sum = sum + remainder
        n //= 10
    print(sum, "is the sum of the number")

sumOfNumber(123)