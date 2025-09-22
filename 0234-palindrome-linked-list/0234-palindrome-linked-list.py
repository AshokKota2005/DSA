# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head
        result = []
        while head:
            result.append(head.val)
            head = head.next
        i,j = 0,len(result)-1
        while i <= j:
            if result[i] != result[j]:
                return False
            i = i+1
            j = j-1
        return True


        