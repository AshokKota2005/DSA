# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        if head is None:
            return None
        if head.next is None:
            if head.val == val:
                return None
            else:
                return head
        while head:
            if head.val != val:
                dummy.next = head
                dummy = dummy.next 
            head = head.next
        dummy.next = None
        return tail.next
        