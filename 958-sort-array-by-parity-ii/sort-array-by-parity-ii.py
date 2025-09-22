class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        a = 0
        b = 1
        for i in range(0,len(nums)):
            if nums[i]%2 == 0:
                res[a] = nums[i]
                a = a+2
            else: 
                res[b] = nums[i]
                b = b+2
        return res

        