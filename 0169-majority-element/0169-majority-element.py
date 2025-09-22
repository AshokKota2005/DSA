class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for char in nums:
            if(char not in d):
                d[char] = 1
            else:
                d[char] += 1
        list1 = list(d.values())
        max1 = max(list1)
        for char in d:
            if(d[char] == max1):
                return char

