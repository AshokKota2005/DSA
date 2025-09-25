class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        list1 = []
        for i in range(0,len(nums1)):
            if nums1[i] not in nums2:
                list1.append(nums1[i])
        answer.append(list(set(list1)))
        list1 = []
        for i in range(0,len(nums2)):
            if nums2[i] not in nums1:
                list1.append(nums2[i])
        answer.append(list(set(list1)))
        return answer


        