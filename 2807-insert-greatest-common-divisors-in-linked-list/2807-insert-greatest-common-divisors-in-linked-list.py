# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head 
        while head and head.next:
            a = head.val
            b = head.next.val 
            n = min(a,b)
            for i in range(1,n+1):
                if a%i == 0 and b%i == 0:
                    res = i
            new_node = ListNode(res) 
            new_node.next = head.next
            head.next = new_node
            head = head.next.next
        return tail
            
        