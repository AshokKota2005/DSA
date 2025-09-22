class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = 0
        for char in nums:
            length += 1
        add1 = 0
        add2 = 0
        flag = False
        for i in range(0,length):
            for j in range(i+1,length):
                if(target == nums[i]+nums[j]):
                    add1 = i
                    add2 = j
                    flag = True
                    break
            if flag:
                break
        return [add1,add2]


        