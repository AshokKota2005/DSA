class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum1  = 0
        for i in jewels:
            sum1 = sum1 + stones.count(i)
        return sum1
        