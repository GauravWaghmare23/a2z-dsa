a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

i = 0
j = 0
union = []

while i < len(a) and j < len(b):

    if a[i] < b[j]:
        union.append(a[i])
        i += 1

    elif a[i] > b[j]:
        union.append(b[j])
        j += 1

    else:
        union.append(a[i])
        i += 1
        j += 1

while i < len(a):
    union.append(a[i])
    i += 1

while j < len(b):
    union.append(b[j])
    j += 1

print(union)