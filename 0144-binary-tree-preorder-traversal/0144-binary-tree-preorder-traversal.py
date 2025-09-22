# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self,root,stack):
        if root is None:
            return []
        stack.append(root.val)
        self.pre_order(root.left,stack)
        self.pre_order(root.right,stack)
        return stack
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = self.pre_order(root,stack)
        return res
    
