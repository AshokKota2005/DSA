# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        stack = []
        current = root
        result = []
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        result.sort()
        i = 0
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.val != result[i]:
                current.val = result[i]
            i += 1
            current = current.right 
            
         
        