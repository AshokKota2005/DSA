class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum1 = 0
        i = 0
        sum1 = 0
        while(i < len(a)):
            sum1 = sum1 + int(a[i]) * (2**(len(a)-i-1))
            i = i+1
        i = 0
        sum2 = 0
        while(i < len(b)):
            sum2 = sum2 + int(b[i]) * (2**(len(b)-i-1))
            i = i+1
        sum3 = sum1 + sum2
        res = ""
        while sum3> 0:
            res = str(sum3%2)+res
            sum3 = sum3//2
        if res == "":
            return "0"
        else:
            return res

        