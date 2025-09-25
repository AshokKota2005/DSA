class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sum1 = 0
        for i in range(0,len(s)):
            if s[i] in t:
                ind = t.index(s[i])
                sum1 = sum1 + abs(i - ind)
            else:
                sum1 = sum1 + 0
        return sum1
        