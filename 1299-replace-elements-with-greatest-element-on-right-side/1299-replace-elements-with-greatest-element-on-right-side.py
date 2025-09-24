from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        result = [-1] * n
        max_right = -1
        for i in range(n - 1, -1, -1):
            result[i] = max_right
            max_right = max(max_right, arr[i])
        return result
