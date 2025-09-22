class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1,n+1):
            res.append(i)
        res = list(map(str,res))
        res.sort()
        res = list(map(int,res))
        return res
        