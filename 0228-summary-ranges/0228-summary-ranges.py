class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list1 = []
        i = 0
        while i < len(nums):
            first = nums[i]
            flag = True
            res = []
            while flag:
                res.append(str(first))
                first = first + 1
                if first not in nums:
                    flag = False
            if len(res) == 1:
                list1.append(res[0])
            elif len(res) >= 2:
                k = res[0] + '->' + res[-1]
                list1.append(k)
            i = i + len(res) 
        return list1
             
        