num = 12345678987654321

original,rev = num,0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print("Palindrome" if original == rev else "Not a Palindrome")