class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list1 = []
        for i in range(0,len(nums)):
            if nums[i] == target:
                list1.append(i)
        if len(list1) != 0:
            list2 = []
            list2.append(list1[0])
            list2.append(list1[-1])
            return list2
        else:
            return [-1,-1]

        