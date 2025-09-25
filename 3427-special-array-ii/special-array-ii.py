from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        parity_changes = [0] * n
        for i in range(1, n):
            parity_changes[i] = parity_changes[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                parity_changes[i] += 1
        res = []
        for start, end in queries:
            if parity_changes[end] - parity_changes[start] == 0:
                res.append(True)
            else:
                res.append(False)
        return res



        