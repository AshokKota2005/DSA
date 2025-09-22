class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for i in range(left,right+1):
            binary = bin(i)[2:]
            num = binary.count('1')
            i = 1
            c = 0
            while i <= num//2:
                if num%i == 0:
                    c += 1
                i += 1
            if c == 1:
                res += 1
        return res
        