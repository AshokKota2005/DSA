class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        list1 = []
        res = ""
        c = 0
        while len(s) != 0:
            if s[0] == '(':
                c = c+1 
            else:
                c = c-1
            res = res + s[0]
            s = s[1:]
            if c == 0:
                list1.append(res)
                res = ""
        res = ""
        for i in range(0,len(list1)):
            list1[i] = list1[i][1:-1]
        res = "".join(list1)
        return res
        
        