class Solution:
    def thirdMax(self, nums: List[int]) -> int:#[1,1,1,1]
        nums = set(nums)#[1]
        length1 = 0
        for char in nums:
            length1 += 1 #1
        list1 = max(nums)
        nums.remove(list1)
        length1 = length1 - 1
        if(length1 != 0):
            list2 = max(nums)
            nums.remove(list2)
            length1 = length1 - 1
            if(length1!=0):
                list3 = max(nums)
                return list3
            else:
                return list1
        else:
            return list1