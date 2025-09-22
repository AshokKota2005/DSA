class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list3 = []
        for char in nums1:
            for key in nums2:
                if char == key:
                    list3.append(key)
                    nums2.remove(key)
                    break
        return list3



        