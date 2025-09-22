# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        flag = 0
        res = 0
        l3 = []
        while l1 or l2:
            sum1 = 0
            if l1:
                sum1 = sum1 + l1.val
            if l2:
                sum1 = sum1 + l2.val
            if flag == 1:
                sum1 = sum1 + res
                flag = 0
            if len(str(sum1)) > 1:
                flag = 1
                temp = sum1 
                sum1 = sum1%10
                
                res = temp//10
                
            l3.append(sum1)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if flag == 1:
            l3.append(res)
        for i in range(0,len(l3)):
            node  = ListNode(l3[i])
            dummy.next = node 
            dummy = dummy.next
        return head.next

        