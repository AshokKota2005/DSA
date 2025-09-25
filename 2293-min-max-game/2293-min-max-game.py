class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            i = 0
            c = 0
            while i < len(nums)-1:
                if c%2 == 0:
                    nums[i] = min(nums[i],nums[i+1])
                    nums.pop(i+1)
                else:
                    nums[i] = max(nums[i],nums[i+1])
                    nums.pop(i+1)
                c = c+1
                i = i+1
        return nums[0]


        