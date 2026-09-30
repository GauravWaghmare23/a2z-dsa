nums = [3,0,1]

expected_sum = len(nums) * (len(nums) + 1) // 2
actual_sum = 0

for i in range(len(nums)):
    actual_sum += nums[i]
    
print(expected_sum - actual_sum)