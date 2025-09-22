# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]
        def getheight(root):
            if not root:
                return 0
            a = getheight(root.left)
            b = getheight(root.right)
            d = a+b
            if d > max_d[0]:
                max_d[0] = d
            return 1+max(a,b)
        getheight(root) 
        return max_d[0]