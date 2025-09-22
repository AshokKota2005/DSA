class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:] 
        res = ""
        for char in num:
            if char == '0':
                res = res + '1'
            elif char == '1':
                res = res + '0'
        res = res[::-1]
        sum1 = 0
        for i in range(0,len(res)):
            sum1 = sum1 + int(res[i]) * (2**i)
        return sum1