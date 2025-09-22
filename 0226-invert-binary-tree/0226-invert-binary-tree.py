# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        result = []
        dummy = root
        while stack:
            length = len(stack)
            for j in range(0,length):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if node.left or node.right:
                    node.left,node.right = node.right,node.left
        return dummy
        

        