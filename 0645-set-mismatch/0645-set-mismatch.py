class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(1,n+1):
            d[i] = 0
        for i in range(0,len(nums)):
            d[nums[i]] += 1
        a,b= 0,0
        for x in d:
            if d[x] == 0:
                a = x
            if d[x] == 2:
                b = x
        return [b,a]

            