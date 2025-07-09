class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start,end = 0,len(nums)-1
        if target > nums[end]:
            return end + 1
        if target < nums[start]:
            return 0
        while start + 1 < end:
            mid = (start + end) //2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        else:
            return end

        