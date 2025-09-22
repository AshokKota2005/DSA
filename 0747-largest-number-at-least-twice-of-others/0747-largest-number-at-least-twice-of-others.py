class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1 = max(nums)
        c = nums.index(max1)
        for char in nums:
            if (char != max1):
                if(char*2 <= max1):
                    pass
                else:
                    return -1
        return c
        