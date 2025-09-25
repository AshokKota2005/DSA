# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        for i in range(1,count+1):
            c = 0
            list2 = []
            while head and c < i:
                list2.append(head.val)
                head = head.next
                c = c+1 
            if len(list2)%2 != 0:
                list1.extend(list2)
            else:
                list1.extend(list2[::-1])
        dummy = tail = ListNode(0)
        for value in list1:
            dummy.next = ListNode(value)
            dummy = dummy.next
        return tail.next
            
            
        