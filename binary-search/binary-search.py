def search(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = first + (last - first) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            first = mid + 1

        else:
            last = mid - 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

result = search(nums, target)

print("Target index:", result)