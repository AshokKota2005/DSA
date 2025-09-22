class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        i = 0
        while i < len(t): 
            if t[i] not in s:
                return t[i]
            else:
                s = s.replace(t[i],"",1)
                i = i+1

             