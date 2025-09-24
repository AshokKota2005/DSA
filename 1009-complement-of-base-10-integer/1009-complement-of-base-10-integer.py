import math
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)[2:]
        res = ""
        for i in range(0,len(num)):
            if num[i] == '0':
                res = res + '1'
            else:
                res = res + '0'
        res = res[::-1]
        sum1 = 0
        for i in range(0,len(res)):
            sum1 = sum1 + int(res[i]) * (2**i)
        return sum1

        