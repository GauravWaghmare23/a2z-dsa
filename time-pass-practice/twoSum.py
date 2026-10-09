nums = [2, 7, 11, 15]
target = 9

seen = {}

for i,item in enumerate(nums):
    complement = target - item
    print(complement)

    if complement in seen:
        print(seen[complement],i)
        break

    seen[item] = i
    print(seen)