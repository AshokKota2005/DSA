class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for char in s:
            m = ord(char)
            if(m >= 65 and m <= 90):
                m = m + 32
                res = res + chr(m)
            else:
                res = res + chr(m)
        return res
        