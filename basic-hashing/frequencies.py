arr = [2, 3, 2, 3, 5]

hashMap = {}

for i in range(1,len(arr)+1):
    hashMap[i] = 0;

for i in range(len(arr)):
    if arr[i] in hashMap:
        hashMap[arr[i]] += 1
        
print([hashMap])
    