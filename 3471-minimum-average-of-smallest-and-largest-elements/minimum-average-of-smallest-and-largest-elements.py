class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        for i in range(0,len(nums)//2):
            min1 = min(nums)
            nums.remove(min1)
            max1 = max(nums)
            nums.remove(max1)
            averages.append((min1+max1)/2)
        return min(averages)
            