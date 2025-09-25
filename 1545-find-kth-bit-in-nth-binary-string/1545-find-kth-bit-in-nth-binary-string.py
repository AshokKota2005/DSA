class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        for i in range(0,n-1):
            m = ""
            for j in range(len(s)):
                if s[j] == '0':
                    m = m + '1'
                else:
                    m = m + '0'
            m = m[::-1]
            s = s + '1' + m
        return s[k-1]  



        