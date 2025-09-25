class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        for i in range(0,len(s)):
            if s[i] == 'i':
                res = res[::-1]
            else:
                res = res + s[i]
        return res
        