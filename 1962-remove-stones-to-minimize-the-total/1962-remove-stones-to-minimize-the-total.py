import heapq
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        i = 0
        while i < k:
            temp = heapq.heappop(piles)
            temp = math.floor(temp/2) 
            heapq.heappush(piles,temp)
            i += 1
        return -sum(piles)
        