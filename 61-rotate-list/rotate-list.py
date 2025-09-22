# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head 
        if head.next is None:
            return head
        tail = head
        length = 0
        while tail:
            tail = tail.next
            length += 1
        k = k %length
        s = 0
        while(s < k):
            tail = head
            while(tail.next):
                prev = tail
                tail = tail.next
            tail.next = head
            prev.next = None
            head = tail 
            s = s+1
        return head
        
            

        