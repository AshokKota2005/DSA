class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0]
        for i in range(0,len(nums)-1):
            a = nums[i]+leftSum[i]
            leftSum.append(a) 
        rightSum = [0]
        nums = nums[::-1] 
        for i in range(0,len(nums)-1):
            b = rightSum[i] + nums[i]
            rightSum.append(b)
        rightSum = rightSum[::-1]
        ans = []
        for i in range(0,len(nums)):
            ans.append(abs(leftSum[i] - rightSum[i]))
        return ans

        