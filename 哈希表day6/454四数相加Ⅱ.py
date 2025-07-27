class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        hashmap = dict()
        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i+j] += 1
                else:
                    hashmap[i+j] = 1
        count = 0
        for x in nums3:
            for y in nums4:
                key = - x - y
                if key in hashmap:
                    count += hashmap[key]
        return count
