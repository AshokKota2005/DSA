class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        list1 = set(nums)
        for i in list1:
            if nums.count(i) == n:
                return i        