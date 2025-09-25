class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums)):
            if nums.count(nums[i]) == 2:
                if nums[i] not in res:
                    res.append(nums[i])
        return res

        