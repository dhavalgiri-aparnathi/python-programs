def reverseNumber(n):
    sum = 0
    while n != 0:
        remainder = n % 10
        sum = sum * 10 + remainder
        n //= 10
    print(sum, "is the reverse of the number")

reverseNumber(123)