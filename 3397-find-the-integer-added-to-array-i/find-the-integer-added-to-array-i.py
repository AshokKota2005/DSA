class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1 == nums2:
            return 0
        nums1.sort()
        nums2.sort()
        diff = nums2[0] - nums1[0]
        return diff
        