class Solution(object):
    def twoSum(self, nums, target):
        v={}
        for i,num in enumerate(nums):
            r=target-num
            if r in v:
                return [v[r],i]
            v[num]=i