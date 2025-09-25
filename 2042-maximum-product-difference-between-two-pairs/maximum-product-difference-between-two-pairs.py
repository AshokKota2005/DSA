class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        b = nums[1]
        min1 = a* b
        c = nums[-1]
        d = nums[-2]
        max1 = c * d
        return max1-min1
        

