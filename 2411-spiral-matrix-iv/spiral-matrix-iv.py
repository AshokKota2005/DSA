# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix =[]
        for i in range(0,m):
            col = [-1]*n
            matrix.append(col)
        left,right = 0,n
        top,bottom = 0,m
        while head:
            #Left to Right
            for i in range(left,right):
                if not head:
                    return matrix
                matrix[top][i] = head.val
                head = head.next
            top = top+1
            #Top to Bottom.
            for i in range(top,bottom):
                if not head:
                    return matrix
                matrix[i][right-1] = head.val
                head = head.next
            right = right-1
            #Right to Left.
            for i in range(right-1,left-1,-1):
                if not head:
                    return matrix
                matrix[bottom-1][i] = head.val
                head = head.next
            bottom = bottom-1
            #Bottom to Top.
            for i in range(bottom-1,top-1,-1):
                if not head:
                    return matrix
                matrix[i][left] = head.val
                head = head.next
            left = left+1
        return matrix
            

        