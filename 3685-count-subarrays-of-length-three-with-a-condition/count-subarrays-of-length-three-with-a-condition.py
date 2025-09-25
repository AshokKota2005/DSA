class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        list1 = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)+1):
                temp = nums[i:j]
                if len(temp) == 3:
                    list1.append(temp)
        print(list1)
        c = 0
        for i in range(0,len(list1)):
            temp = list1[i]
            a = temp[0] + temp[2]
            b = temp[1]/2
            print(a)
            print(b)
            if a == b:
                c += 1
        return c
            