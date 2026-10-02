nums = [1,1,0,1,1,1]

currentMax = 0
Max = 0

for i in range(len(nums)):
    if nums[i] == 0:

        if Max < currentMax:
            Max = currentMax

        currentMax = 0
    else:
        currentMax += 1

if Max < currentMax:
    Max = currentMax

print(Max)

