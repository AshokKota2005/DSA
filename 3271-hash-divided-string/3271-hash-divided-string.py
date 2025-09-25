class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        while len(s) != 0:
            che = s[:k]
            sum1 = 0
            for i in range(0,len(che)):
                asciii = ord(che[i])-97
                sum1 = sum1 + asciii
            rem = sum1%26
            res = res + chr(rem + 97)
            s = s[k:]
        return res
