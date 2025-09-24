# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        list1 = ""
        while head:
            list1 = list1 + str(head.val)
            head = head.next 
        i = 0
        sum1 = 0
        while(i < len(list1)):
            sum1 = sum1 + int(list1[i]) * (2**(len(list1)-i-1))
            i = i+1
        return sum1
        