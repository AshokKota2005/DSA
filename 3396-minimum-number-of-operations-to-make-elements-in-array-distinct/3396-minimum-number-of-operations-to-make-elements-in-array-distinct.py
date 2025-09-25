class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        while len(nums) != 0:
            numss = list(set(nums))
            if len(numss) == len(nums):
                return c
            else:
                if len(nums) >= 3:
                    nums = nums[3:]
                    c += 1
                else:
                    c += 1
                    return c        
        return c