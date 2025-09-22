class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1 = [ ]
        list1 = list(map(str,s.split()))
        return len(list1[-1])
        