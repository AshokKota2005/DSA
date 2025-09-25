class Solution:
    def countElements(self, nums: List[int]) -> int:
        min1 = min(nums)
        max1 = max(nums)
        c = 0
        for i in range(0,len(nums)):
            if (nums[i] > min1 and nums[i] < max1):
                c += 1
        return c
       
        