class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        c = 0
        for i in range(0,len(s)):
            if s[i] == 'R':
                c = c-1
            else:
                c = c+1
            if c == 0:
                res += 1
        return res
        