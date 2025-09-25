class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(0,n):
            k = start + 2 * i 
            nums.append(k)
        res = 0
        for i in range(0,len(nums)):
            res = res ^ nums[i]
        return res
