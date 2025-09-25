# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        c = 1
        while list1:
            if c < a:
                list1 = list1.next
                c = c+1
            else:
                current = list1.next
                while c < b:
                    current = current.next
                    c = c+1
                list1.next = list2
                while list1.next:
                    list1 = list1.next
                list1.next = current.next
                break
        return head



        