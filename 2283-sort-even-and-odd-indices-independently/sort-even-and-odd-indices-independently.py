class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(0,len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        res = [0]*len(nums)
        a,b = 0,0
        for i in range(0,len(nums)):
            if i%2 == 0:
                res[i] = even[a]
                a = a+1
            else:
                res[i] = odd[b]
                b = b+1
        return res

        