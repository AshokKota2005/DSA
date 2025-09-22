# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        tail = head
        while head:
            count += 1
            head = head.next
        head = tail
        target = (count//2)+1
        k =  1
        while k < target:
            head = head.next
            k += 1
        return head
        