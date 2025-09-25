# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list2 = []
        length = len(list1) 
        for i in range(0,(length//2)):
            sum1 = list1[i]+list1[length-1-i]
            list2.append(sum1)
        res = max(list2)
        return res
        

       
        

        