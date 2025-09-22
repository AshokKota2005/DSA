class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p1 = set(pattern)
        s1 = s.split(" ")
        s2 = set(s1)
        if len(p1) != len(s2):
            return False
        if len(pattern) == len(s1):
            d = {}
            for i in range(0,len(pattern)):
                if pattern[i] not in d.keys():
                    if s1[i] not in d.values():
                        d[pattern[i]] = s1[i]
                else:
                    temp = d[pattern[i]]
                    if temp != s1[i]:
                        return False
            return True
        else:
            return False