# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        stack = []
        current = root
        result = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.val in result:
                return True
            else:
                result.append(k-current.val)
            current = current.right
        return False