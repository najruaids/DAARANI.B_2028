def searchInsert(nums,target):
    for i in range(len(nums)):
        if nums[i]>=target:
            return i
    return len(nums)
n=list(map(int,input().split()))
target=int(input())
print(searchInsert(n,target))