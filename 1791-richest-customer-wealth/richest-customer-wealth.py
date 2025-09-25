class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for i in range(0,len(accounts)):
            sum1 = 0
            for j in range(0,len(accounts[0])):
                sum1 = sum1 + accounts[i][j]
            res.append(sum1)
        return max(res)
