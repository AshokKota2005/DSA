# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy  
        list1 = []
        c = 1
        k = 0
        while head:
            if c%2 == 0:
                list1.append(head.val)
            else:
                list1.insert(k,head.val)
                k = k+1
            c = c+1
            head = head.next
        for i in list1:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return tail.next
        