class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res1 = ""
        res2 = ""
        while x > 0 or y > 0:
            res1 = str(x%2) + res1
            res2 = str(y%2) + res2
            x = x//2
            y = y//2
        c = 0
        for i in range(0,len(res1)):
            if(res1[i] != res2[i]):
                c += 1
        return c

        

        