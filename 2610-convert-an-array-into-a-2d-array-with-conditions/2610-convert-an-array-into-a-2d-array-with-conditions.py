class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while len(nums) != 0:
            list1 = []
            for i in range(0,len(nums)):
                if nums[i] not in list1:
                    list1.append(nums[i])
            res.append(list1)
            for i in range(0,len(list1)):
                nums.remove(list1[i])
        return res

        