class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        k = len(nums)-1
        c = 0
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(0,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        if i < j and j < k:
                            c = c+1
        return c
        