nums = [0,0,1,1,1,2,2,3,3,4]

seen = set()
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result.__len__(),result)