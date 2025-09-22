class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        flag = True
        j = 0
        for i in range(0,len(s)):
            flag = True
            while flag and j < len(t):
                if s[i] == t[j]:
                    flag = False
                j = j+1
        if flag == False and i == len(s)-1:
            return True
        else:
            return False