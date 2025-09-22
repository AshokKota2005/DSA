# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        result = []
        while headA:
            result.append(headA)
            headA = headA.next
        while headB:
            if headB not in result:
                headB = headB.next
            else:
                return headB
        return None 
        

        
        