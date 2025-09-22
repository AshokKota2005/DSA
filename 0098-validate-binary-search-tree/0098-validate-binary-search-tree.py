# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
            return stack
        inorder(root)
        res1 = sorted(stack)
        res2 = list(set(res1))
        if res1 == stack and len(res1) == len(res2):
            return True
        else:
            return False