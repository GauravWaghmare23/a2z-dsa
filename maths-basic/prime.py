num = 44

flag = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        flag = False
        break

print(flag)
