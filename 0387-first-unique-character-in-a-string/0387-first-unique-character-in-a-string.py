class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        res = ""
        for key in d.keys():
            if d[key] == 1:
                res = res + key
                break
        if (res != ""):
            return s.index(str(res))
        else:
            return -1
        