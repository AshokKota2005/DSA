class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length1 = 0
        for char in nums:
            length1 += 1
        if(length1 == 0):
            return " "
        for i in range(0,length1 + 1):
            if(i not in nums):
                return i
            