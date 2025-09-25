class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum1 = 0
        num = set(nums)
        for i in num:
            check = nums.count(i)
            if check == 1:
                sum1 = sum1 + i
        return sum1
        