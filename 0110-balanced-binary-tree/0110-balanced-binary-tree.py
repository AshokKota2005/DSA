# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getheight(self,root):
        if root is None:
            return [True,0]
        a = self.getheight(root.left)
        b = self.getheight(root.right) 
        balanced = (a[0] and b[0] and abs(a[1] - b[1]) <= 1 )
        return [balanced, 1+max(a[1],b[1])]  

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        res = self.getheight(root)
        return res[0]