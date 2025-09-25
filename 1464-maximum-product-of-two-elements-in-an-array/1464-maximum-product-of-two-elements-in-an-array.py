class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = []
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                res.append((nums[i]-1)*(nums[j]-1))
        return max(res)

        