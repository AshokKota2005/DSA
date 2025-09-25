# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        list1 = []
        ress = [-1,-1]
        while head:
            list1.append(head.val)
            head = head.next
        res = []
        if len(list1) > 2:
            for i in range(1,len(list1)-1):
                if list1[i] > list1[i-1] and list1[i] > list1[i+1] or list1[i] < list1[i-1] and list1[i] < list1[i+1]:
                    res.append(i)
        else:
            return ress
        if len(res) != 0:
            max1 = -1
            if len(res) > 1:
                max1 = res[-1] - res[0]
            min1 = float(inf)
            for i in range(0,len(res)-1):
                diff = res[i+1] - res[i]
                if diff < min1:
                    min1 = diff
            if min1 != float(inf):
                return [min1,max1]
            else:
                return [-1,max1]
        else:
            return ress

        
                
            


        