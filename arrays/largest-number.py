arr = [4, 7, 2, 9, 1]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)