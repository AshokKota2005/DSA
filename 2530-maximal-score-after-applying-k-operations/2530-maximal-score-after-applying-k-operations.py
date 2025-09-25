import heapq
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums =  [-num for num in nums]
        heapq.heapify(nums)
        i = 0
        count = 0
        while i < k:
            temp = heapq.heappop(nums) 
            count += temp
            temp = math.floor(temp/3) 
            heapq.heappush(nums,temp)
            i += 1
        return -count
        