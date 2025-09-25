class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}
        nums1.extend(nums2)
        for x in nums1:
            if x[0] not in d:
                d[x[0]] = x[1]
            else:
                d[x[0]] += x[1]
        d = dict(sorted(d.items())) 
        list1 = []
        for x in d:
            res = [x,d[x]]
            list1.append(res)
        return list1

        