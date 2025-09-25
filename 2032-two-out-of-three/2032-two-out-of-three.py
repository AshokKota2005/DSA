class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        list1 = nums1+nums2+nums3
        res = []
        for i in range(0,len(list1)):
            if list1[i] in nums1 and list1[i] in nums2:
                res.append(list1[i])
            elif list1[i] in nums2 and list1[i] in nums3:
                res.append(list1[i])
            elif list1[i] in nums1 and list1[i] in nums3:
                res.append(list1[i])
        res = list(set(res))
        return res
