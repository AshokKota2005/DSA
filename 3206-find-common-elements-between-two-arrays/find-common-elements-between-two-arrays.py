class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = 0
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                a = a+1
               
        b = 0
        for i in range(0,len(nums2)):
            if nums2[i] in nums1:
                b = b+1
              
        return [a,b]        

        