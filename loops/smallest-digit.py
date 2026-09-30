num = int(input())
smallest = 9

while num > 0:
    ld = num % 10
    if smallest > ld:
        smallest = ld
    num = num // 10

print(smallest)
    