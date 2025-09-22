import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list(itertools.permutations(nums))
        res = set(res)
        res = list(res)
        return res