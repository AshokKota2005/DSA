class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        length = len(n)
        sum1 = 0
        for i in range(0,length):
            if (i%2 == 0):
                sum1 = sum1 + int(n[i])
            else:
                sum1 = sum1 - int(n[i])
        return sum1
        