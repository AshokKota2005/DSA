class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        list1 = []
        for char in nums:
            list1.append(char*char)
        return sorted(list1)

        