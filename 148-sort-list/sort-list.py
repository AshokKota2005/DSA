# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None:
                return head
            list1 = []
            while head:
                list1.append(head.val)
                head = head.next
            list1.sort()
            dummy = tail = ListNode(0)
            for val in list1:
                node = ListNode(val)
                dummy.next = node
                dummy = dummy.next
            return tail.next
        