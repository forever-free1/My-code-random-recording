class Solution(object):
    def twoSum(self, nums, target):
        idx = {}
        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x],j]
            idx[x] = j