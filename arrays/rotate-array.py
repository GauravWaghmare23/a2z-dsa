nums = [-1,-100,3,99]
k = 2

def reverse(first,last,arr):
    while first < last:
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp
        
        first += 1
        last -= 1
        
reverse(0,len(nums)-1,nums)
reverse(0,k-1,nums)
reverse(k,len(nums)-1,nums)

print(nums)