"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
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
        return len(result)
        