import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts) 
        i = 0
        while i < k:
            temp = heapq.heappop(gifts)
            temp = -temp 
            temp = math.floor(temp ** (1/2))
            i += 1
            heapq.heappush(gifts,-temp) 
        return -sum(gifts)
          