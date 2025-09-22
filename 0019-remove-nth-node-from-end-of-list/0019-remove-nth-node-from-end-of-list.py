# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail  = head
        count = 0
        while head:
            count = count+1
            head = head.next
        head = tail
        flag = count - n 
        if flag > 0:
            sk = 1
            while sk < flag:
                head = head.next 
                sk += 1 
            head.next = head.next.next
            return tail 
        else:
            head = head.next
            return head

            

            