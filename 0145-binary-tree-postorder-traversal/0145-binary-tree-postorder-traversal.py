# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root,stack):
        if root is None:
            return []
        self.postorder(root.left,stack)
        self.postorder(root.right,stack)
        stack.append(root.val)
        return stack

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = self.postorder(root,stack)
        return res
        