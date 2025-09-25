import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums) 
        count = 0
        sum1 = current_sum = sum(nums)
        sum1 = sum1/2 
        while current_sum < sum1: 
            temp = -heapq.heappop(nums) 
            temp = temp/2
            heapq.heappush(nums,-temp)
            current_sum = current_sum + temp
            count += 1
        return count
        