nums = [4,1,2,1,2]

sets = set()

for num in nums:
    if num in sets:
        sets.remove(num)
    else :
        sets.add(num)
        
print(sets.pop())