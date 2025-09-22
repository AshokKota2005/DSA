# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def height(root,cur_sum):
            if root is None:
                return False
            cur_sum += root.val
            if root.left is  None and root.right is None:
                return targetSum == cur_sum
            return height(root.left,cur_sum) or height(root.right,cur_sum)
        return height(root,0)
                    
        