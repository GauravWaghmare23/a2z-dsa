num = int(input())
big = 0

while num > 0:
    ld = num % 10
    if big < ld:
        big = ld
    num = num // 10

print(big)
    