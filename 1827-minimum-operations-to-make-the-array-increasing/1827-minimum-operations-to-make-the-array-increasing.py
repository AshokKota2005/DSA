class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1] = nums[i+1] + 1
                res = res + 1
            if not nums[i] < nums[i+1]:
                diff = (nums[i] - nums[i+1]) + 1
                nums[i+1] = nums[i+1] + diff
                res = res + diff
        return res