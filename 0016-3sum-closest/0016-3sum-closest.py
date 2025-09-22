class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float(inf)
        i = 0
        while i < len(nums)-2:
            left,right = i+1,len(nums)-1
            while left < right:
                sum1 = nums[i] + nums[left] + nums[right]
                if(abs(sum1 - target) < abs(close_sum - target)):
                    close_sum = sum1
                if sum1 < target:
                    left += 1
                else:
                    right -= 1
            i += 1
        return close_sum
        
        