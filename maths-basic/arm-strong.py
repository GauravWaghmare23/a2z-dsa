num = 153
original = num
total = 0

while num > 0:
    digit = num % 10
    total += digit * digit * digit
    num //= 10

if original == total:
    print("Armstrong Number")
else:
    print("Not Armstrong number")