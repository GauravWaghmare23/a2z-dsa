nums = [4,1,2,1,2]

sets = set()

for i in range(len(nums)):
    if nums[i] in sets:
        sets.remove(nums[i])
    else:
        sets.add(nums[i])

print(sets.pop())