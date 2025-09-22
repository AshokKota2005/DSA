class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = set(s)
        t1 = set(t)
        if len(s1) != len(t1):
            return False
        if len(s) == len(t):
            d = {}
            for i in range(0,len(s)):
                if s[i] not in d:
                    d[s[i]] = t[i]
                else:
                    check = d[s[i]]
                    if check != t[i]:
                        return False
            return True
        else:
            return False
        