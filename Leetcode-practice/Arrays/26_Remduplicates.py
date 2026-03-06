class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        k = 0
        nums[k] = nums[0]
        k += 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k