# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        length = len(list1)
        length = length//2
        list2 = []
        list2.extend(list1[:length]) 
        list2.extend(list1[length+1:]) 
        dummy = tail = ListNode(0)
        for value in list2:
            dummy.next = ListNode(value)
            dummy = dummy.next
        return tail.next
        
        