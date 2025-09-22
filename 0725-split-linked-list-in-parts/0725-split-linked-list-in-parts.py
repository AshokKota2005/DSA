import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        num = math.floor(count/k)
        nums = math.floor(count%k)
        result = []
        while head:
            flag = True
            if len(result) < nums:
                num = num + 1
                flag = False
            res = [] 
            for i in range(0,num):
                res.append(head)
                if len(res) == num:
                    prev = head
                    head = head.next
                    prev.next = None
                else:
                    head = head.next 
            result.append(res[0]) 
            if flag == False:
                num = num - 1
        while len(result) < k:
            result.append(None)
        return result
        