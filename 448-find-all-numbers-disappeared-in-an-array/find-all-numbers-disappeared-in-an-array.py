class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length1 = len(nums)
        '''list1 = []
        for i in range(1,length1+1):
            if(i not in nums):
                list1.append(i)
        return list1'''
        l=set(range(1,length1+1))
        nums=set(nums)
        l=list(l-nums)
        l.sort()
        return l

        