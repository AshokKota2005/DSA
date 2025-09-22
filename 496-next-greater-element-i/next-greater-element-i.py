class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 =[]
        flag1 = 0 
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if(nums1[i] == nums2[j]):
                    flag1 = 0
                    for k in range(j+1,len(nums2)):
                        if(nums2[k] > nums2[j]):
                            list1.append(nums2[k])
                            flag1 = 1
                            break
                        else:
                            pass
                    if(flag1 == 0):
                        list1.append(-1)
                    break
        return list1
                