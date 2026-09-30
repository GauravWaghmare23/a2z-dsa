nums = [3,4,5,1,2]

count = 0

for i in range(len(nums)):
    if nums[i] > nums[(i+1) % len(nums)]:
          count += 1

if count > 1:
    print("Not rotated and sorted")
else:
    print("Rotated and sorted")