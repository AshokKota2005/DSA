class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ss = 1 << len(nums)
        for i in range(0,ss):
            list1 = []
            for j in range(0,len(nums)):
                if i & (1 << j):
                    list1.append(nums[j])
            ans.append(list1)
        return ans        