class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = [],[]
        for i in range(0,len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        res = [0]*len(nums)
        a,b = 0,0
        for i in range(0,len(nums)):
            if i%2 == 0:
                res[i] = pos[a]
                a = a+1
            else:
                res[i] = neg[b]
                b = b+1
        return res
