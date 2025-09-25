class Solution:
    def scoreOfString(self, s: str) -> int:
        res = []
        for i in s:
            res.append(ord(i)) 
        sum1 = 0
        for i in range(0,len(res)-1):
            sum1 = sum1 + abs(res[i] - res[i+1]) 
        return sum1

        