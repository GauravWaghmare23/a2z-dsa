arr = [8, 8, 7, 6, 5]

secondLargest = 0
largest = 0

for i in range(len(arr)):
    if largest < arr[i]:
        secondLargest = largest
        largest = arr[i]
    elif arr[i] > secondLargest and largest > arr[i]:
        secondLargest = arr[i]
        
print(secondLargest);