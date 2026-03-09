def singleNumber(nums):
    res = 0
    for x in nums:
        res ^= x
    return res
n=list(map(int,input().split()))
print(singleNumber(n))