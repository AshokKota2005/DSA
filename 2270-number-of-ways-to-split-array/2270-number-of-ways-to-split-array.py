class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        sum1 = sum(nums)
        sum2 = 0
        for i in range(0,len(nums)-1):
            sum2 += nums[i]
            diff = sum1 - sum2
            if sum2 >= diff:
                count += 1
        return count

        