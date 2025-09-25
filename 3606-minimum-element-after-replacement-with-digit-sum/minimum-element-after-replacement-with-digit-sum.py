class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            sum1 = 0
            while nums[i] > 0:
                r = nums[i]%10
                sum1 = sum1 + r
                nums[i] = nums[i]//10
            nums[i] = sum1
        return min(nums)

        