class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(0,len(nums)):
            list1 = bin(i)[2:]
            if list1.count('1') == k:
                res = res + nums[i]
        return res

              