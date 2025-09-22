"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return 
        stack = [root]
        result = []
        while stack:
            length = len(stack)
            res = []
            for j in range(0,length):
                node = stack.pop(0)
                res.append(node.val)
                if node.children:
                    stack.extend(node.children)
            result.append(res)
        return result