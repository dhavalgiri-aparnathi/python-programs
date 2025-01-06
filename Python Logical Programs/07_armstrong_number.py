def isArmstrongNumber(n):
    sum = 0
    temp = n
    while n != 0:
        remainder = n % 10
        sum = sum + (remainder * remainder * remainder)
        n = n // 10
    if temp == sum: return 1 
    else: return -1

num = int(input("Enter Any Number: "))
res = isArmstrongNumber(num)
print("\nNumber is Armstrong") if res == 1 else print("\nNumber is NOT Armstrong")