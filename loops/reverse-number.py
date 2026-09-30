num = int(input("Enter number: "))

sign = -1 if num < 0 else 1
num = abs(num)

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

rev *= sign

# 32-bit signed integer range
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print(rev)