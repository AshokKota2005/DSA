class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        while 0 in nums:
            nums.remove(0)
            c = c+1
        num1 = [0]*c
        nums.extend(num1)
        """
        Do not return anything, modify nums in-place instead.
        """
        