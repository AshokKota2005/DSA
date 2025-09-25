class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        m = 0
        for i in range(0,len(spaces)):
            k = spaces[i]
            res = res + s[m:k]
            res = res + " "
            m = spaces[i]
        res = res + s[m:]
        return res
            