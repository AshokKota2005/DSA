class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        list1 = []
        for i in range(1 << len(nums)):
            res = []
            for j in range(len(nums)):
                if i & (1 <<j): 
                    res.append(nums[j])
            list1.append(res)
        list2 = []
        for i in range(0,len(list1)):
            sum1 = 0
            for j in range(0,len(list1[i])):
                sum1 = sum1 | list1[i][j]
            list2.append(sum1)
        max1 = max(list2)
        return list2.count(max1)