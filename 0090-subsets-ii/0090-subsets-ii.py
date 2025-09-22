class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        list1 = []
        for i in range(1 << len(nums)):
            sum1 = []
            for j in range(len(nums)):
                if i & (1 << j):
                    sum1.append(nums[j])
            sum1.sort()
            if sum1 not in list1:
                list1.append(sum1)
        return list1
        