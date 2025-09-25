class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max1 = max(candies) 
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >= max1:
                res.append(True)
            else:
                res.append(False)
        return res


            
        