class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        for char in nums:
            sum1 = sum1 + char
            char = str(char)
            for key in char:
                sum2 = sum2+int(key)
        return abs(sum1 - sum2)        