nums = [1,2,3,4,5]

flag = True

for i in range(len(nums)-1):
    if nums[i] >= nums[(i+1)]:
          flag = False
          break

if flag == False:
    print("Not Sorted Array")
else:
    print("Sorted Array")