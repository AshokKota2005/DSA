class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for char in nums:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for key in d.keys():
            if d[key] >= 2:
                return True
        return False
        