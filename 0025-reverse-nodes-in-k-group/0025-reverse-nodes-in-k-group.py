# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list2 = []
        result = []
        for i in range(0,len(list1)):
            list2.append(list1[i])
            if len(list2) == k:
                result.extend(list2[::-1])
                list2 = []
        result.extend(list2)
        tail = dummy = ListNode(0)
        for i in result:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return tail.next   