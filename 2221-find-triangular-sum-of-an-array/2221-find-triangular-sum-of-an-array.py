class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            res = nums[0]+nums[1]
            if len(str(res)) != 1:
                res = res%10
            return res
        else:
            while(len(nums) != 1):
                for i in range(0,len(nums)-1):
                    res = nums[i] + nums[i+1]
                    if len(str(res)) != 1:
                        res = res%10
                    nums[i] = res
                nums.pop()
        return nums[0]

        