class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        list1 = []
        for i in range(len(nums)):
            temp = str(nums[i])
            temp = list(temp)
            temp = list(map(int,temp))
            temp = sum(temp)
            list1.append(temp)
        max_sum = -1
        d = {}
        for i in range(0,len(list1)):
            if  list1[i] in d:
                temp = nums[i] + d[list1[i]]
                if temp > max_sum:
                    max_sum = temp
                if nums[i] > d[list1[i]]:   
                    d[list1[i]] = nums[i]   
            else:
                d[list1[i]] = nums[i]       
        if max_sum >= 0:
            return max_sum
        else:
            return -1

