class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        print(len(nums))
        sum1 = 0
        nums.sort()
        i = 0
        j = 2
        while i < len(nums):
            min1 = min(nums[i:j])
            sum1 = sum1 + min1
            i = j
            j = j+2
        return sum1