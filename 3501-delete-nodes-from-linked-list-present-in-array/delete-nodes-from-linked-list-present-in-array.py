# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0,head)
        prev = dummy
        current = head
        while current:
            if current.val in nums:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return dummy.next
        




                
             




        