nums = [5,3,8,1,2]

for i in range(len(nums)):
    min = i
    for j in range(i+1,len(nums)):

        if nums[j] < nums[min]:
            min = j;

    nums[min],nums[i] = nums[i],nums[min]

print(nums)