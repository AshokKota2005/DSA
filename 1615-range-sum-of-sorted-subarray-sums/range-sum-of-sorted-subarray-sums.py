class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        list1 = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                list1.append(sum(nums[i:j]))
        sum1 = 0
        list1.sort()
        for i in range(left-1,right):
            sum1 += list1[i]
        if len(str(sum1)) > len(str(1000000007)):
            sum1 = sum1 % 1000000007
        return sum1