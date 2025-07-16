class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = set(nums1)
        rec = []
        for x in nums2:
            if x in st:
                st.remove(x)
                rec.append(x)
        return rec
