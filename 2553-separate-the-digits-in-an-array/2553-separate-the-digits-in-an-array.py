class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        list1 = []
        for char in nums:
            m = str(char)
            for key in m:
                list1.append(int(key))
        return list1









           