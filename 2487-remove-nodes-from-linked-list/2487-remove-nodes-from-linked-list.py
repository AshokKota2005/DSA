# Definition for singly-linked list.
# class ListNode:
#     def _init_(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        max_val = float('-inf')
        dummy = ListNode(0)
        tail = dummy   
        while prev:
            if prev.val >= max_val:
                max_val = prev.val
                tail.next = prev
                tail = tail.next
            prev = prev.next
        tail.next = None
        prev = None
        curr = dummy.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev