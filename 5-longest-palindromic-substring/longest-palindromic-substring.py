class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                k = s[i:j]
                if k == k[::-1]:
                    if len(k) > len(res):
                        res = k
        return res
        

        