arr = [8, 8, 7, 6, 5]

largest = 0
secondLargest = 0


for i in range(len(arr)):
    if largest < arr[i]:
        secondLargest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i] > secondLargest:
        secondLargest = arr[i]

print(secondLargest)