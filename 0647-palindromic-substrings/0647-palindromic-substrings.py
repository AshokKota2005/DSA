class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                k = s[i:j]
                if k == k[::-1]:
                    res += 1
        return res
        