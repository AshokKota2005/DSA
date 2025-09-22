class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        i,temp = 0,0
        while i < len(nums) - 1:
            if len(nums) <= 2:
                if nums[0] == nums[1]:
                    return 1
                else:
                    return len(nums)
            else:
                prev = temp
                temp = nums[i+1] - nums[i]
                if i != 0:
                    if temp > 0 and prev < 0 or temp < 0 and prev > 0:
                        i += 1
                    else:
                        nums.pop(i)
                        i = 0
                        temp = 0
                else:
                    i += 1   
        return len(nums)
        