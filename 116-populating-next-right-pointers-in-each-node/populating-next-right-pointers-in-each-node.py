"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        dummy = root
        stack = [root]
        while stack:
            length = len(stack)
            res = []
            for j in range(0,length):
                node = stack.pop(0) 
                if j+1 < length:
                    node.next = stack[0] 
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            stack.extend(res)
        return dummy
            
       
