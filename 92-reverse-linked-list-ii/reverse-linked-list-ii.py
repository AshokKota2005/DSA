# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        list1 = []
        while head:
            list1.append(head.val)
            head = head.next
        left,right = left-1,right-1
        while left <= right:
            list1[left],list1[right] = list1[right],list1[left]
            left,right = left+1,right-1
        print(list1)
        dummy = ListNode(0)
        tail = dummy
        for val in list1:
            node = ListNode(val)
            dummy.next = node
            dummy = dummy.next
        return tail.next
        

        