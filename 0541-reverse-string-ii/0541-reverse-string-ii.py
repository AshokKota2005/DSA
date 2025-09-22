class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        temp = ""
        j = 0
        for i in range(0,len(s)):
            if len(temp) == k:
                if j%2 == 0:
                    res = res + temp[::-1]
                elif j%2 != 0:
                    res = res + temp
                temp = ""
                j = j+1
            temp = temp + s[i] 
        if len(temp) != 0: 
            if len(temp) <= k and j%2 == 0:
                res = res + temp[::-1]
            elif len(temp) <= k and j%2 != 0:
                res = res + temp
            else:
                res = res + temp
        return res
            

                
        