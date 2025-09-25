class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        min1 = min(nums)
        while min1 < k:
            nums.remove(min1)
            count = count + 1
            min1 = min(nums)
        return count