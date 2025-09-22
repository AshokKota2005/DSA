# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list1.sort()
        dummy = ListNode(0)
        tail = dummy
        for i in range(0,len(list1)):
            temp = ListNode(list1[i])
            dummy.next = temp
            dummy = dummy.next
        return tail.next
        