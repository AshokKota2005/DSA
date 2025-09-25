class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for char in s:
            m = ord(char)
            m = m - 96
            res = res + str(m)
        res = int(res)
        for i in range(0,k):
            sum1 = 0
            while(res>0):
                rem = res%10
                sum1 = sum1+rem
                res = res//10
            res = sum1
        return res
        