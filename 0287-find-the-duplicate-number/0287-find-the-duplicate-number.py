class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for char in nums:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in d:
            if d[char] >= 2:
                return char
        