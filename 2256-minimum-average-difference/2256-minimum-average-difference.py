import math
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        llen = 0 
        rlen = len(nums) 
        sum1 = sum(nums)
        sum2 = 0
        list1 = []
        for i in range(0,len(nums)):
            sum2 = sum2 + nums[i] 
            diff = sum1 - sum2
            llen += 1
            rlen -= 1
            a = math.floor(sum2 /llen)
            if rlen != 0:
                b = math.floor(diff /rlen)
            else:
                b = 0
            list1.append(abs(a-b))
        min1 = min(list1)
        ind = list1.index(min1)
        return ind

        