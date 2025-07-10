class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        total = 0
        s_arr = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                s_arr = min(s_arr,right - left + 1)
                total -= nums[left]
                left += 1
        return s_arr if s_arr != float('inf') else 0