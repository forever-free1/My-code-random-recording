def lower_bound(nums: List[int], target: int) -> int:
    left, right = -1, len(nums) 
    while left + 1 < right: 
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid 
        else:
            right = mid 
    return right 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = lower_bound(nums,target + 1) - 1
        return [start,end]