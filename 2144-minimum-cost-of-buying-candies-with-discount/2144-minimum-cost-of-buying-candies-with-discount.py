class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        i = 1
        res = 0
        while i < len(cost)+1:
            if i%3 != 0:
                res = res + cost[i-1]
            i += 1
        return res


        