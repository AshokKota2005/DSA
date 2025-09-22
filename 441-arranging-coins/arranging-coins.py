class Solution:
    def arrangeCoins(self, n: int) -> int:
        if (n ==1 or n==2):
            return 1
        for i in range(1,n+1):
            if i*(i+1)//2>n:
                return i-1