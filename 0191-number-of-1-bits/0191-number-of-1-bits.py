class Solution:
    def hammingWeight(self, n: int) -> int:
        res = ""
        while n> 0:
            res = str(n%2)+res
            n = n//2
        count = 0
        for i in res:
            if i == '1':
                count += 1
        return count
        