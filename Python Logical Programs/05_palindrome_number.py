def isPalindromeNumber(n):
    sum = 0
    temp = n
    while n != 0:
        remainder = n % 10
        sum = sum * 10 + remainder
        n = n // 10
    if temp == sum: return 1 
    else: return -1

num = int(input("Enter Any Number: "))
res = isPalindromeNumber(num)
print("\nNumber is Palindrome") if res == 1 else print("\nNumber is NOT Palindrome")