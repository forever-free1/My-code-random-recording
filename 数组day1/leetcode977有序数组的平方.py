class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left,right = 0,n-1
        result = [0]*n
        pos = n-1
        while left <= right:
            left_sq = nums[left]**2
            right_sq = nums[right]**2
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
        return result
