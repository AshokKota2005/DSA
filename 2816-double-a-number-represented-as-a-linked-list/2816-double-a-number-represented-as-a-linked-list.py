# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val == 0:
            node = ListNode(0)
            return node
        list1 = ""
        while head:
            list1 = list1 + str(head.val)
            head = head.next
        #converting the number in string format to integer format.
        result = 0
        for char in list1:
            result = result * 10 + (ord(char) - ord('0')) 
        result = 2 * result
        #converting the number in integer format to string format.
        res = []
        while result > 0:
            res.append(chr(ord('0') + result % 10))
            result //= 10
        res = res[::-1]
        dummy = ListNode(0)
        tail = dummy
        for value in res:
            dummy.next = ListNode(value)
            dummy = dummy.next
        return tail.next
        