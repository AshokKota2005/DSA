import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while len(nums) > 1:
            temp1 = heapq.heappop(nums)
            temp2 = heapq.heappop(nums) 
            if temp1 < k:
                heapq.heappush(nums,temp1*2+temp2)
                count += 1 
            else:
                break
        return count
        