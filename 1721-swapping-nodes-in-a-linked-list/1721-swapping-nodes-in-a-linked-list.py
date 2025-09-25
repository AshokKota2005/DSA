# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1[k-1],list1[-k] = list1[-k],list1[k-1]
        dummy = ListNode(0)
        tail = dummy
        for i in list1:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return tail.next

        