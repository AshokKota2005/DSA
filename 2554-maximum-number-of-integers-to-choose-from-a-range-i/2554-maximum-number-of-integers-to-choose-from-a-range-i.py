class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = set()
        for i in range(0,len(banned)):
            if banned[i] <= n:
                res.add(banned[i])
        list1 = []
        for i in range(1,n+1):
            sum1 = 0
            if i not in res:
                sum1 = sum(list1)
                sum1 = sum1 + i
                if sum1 <= maxSum:
                    list1.append(i)
        return len(list1)     