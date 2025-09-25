# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        list2 = []
        i = 0
        sum1 = 0
        list1 = list1[1:]
        while i < len(list1):
            if list1[i] != 0:
                sum1 += list1[i]
            else:
                list2.append(sum1)
                sum1 = 0
            i = i+1
        dummy = ListNode(0)
        tail = dummy
        for value in list2:
            dummy.next = ListNode(value)
            dummy = dummy.next
        return tail.next


        