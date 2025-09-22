class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for char  in nums:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
                if d[char] == 2:
                    res.append(char)
        return res
        