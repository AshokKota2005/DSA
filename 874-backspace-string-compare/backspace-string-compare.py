class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)
        i = 0
        res1 = ""
        while(i < a):
            if(s[i] != '#'):
                res1 = res1 + s[i]
            else:
                res1 = res1[::-1]
                if(len(res1) > 1):
                    res1 = res1[1:]
                    res1 = res1[::-1]
                else:
                    res1 = ""
            i = i+1
        i = 0
        res2 = ""
        while(i < b):
            if(t[i] != '#'):
                res2 = res2 + t[i]
            else:
                res2 = res2[::-1]
                if(len(res2) > 1):
                    res2 = res2[1:]
                    res2 = res2[::-1]
                else:
                    res2 = ""
            i = i+1
        if(res1 == res2):
            return True
        else:
            return False