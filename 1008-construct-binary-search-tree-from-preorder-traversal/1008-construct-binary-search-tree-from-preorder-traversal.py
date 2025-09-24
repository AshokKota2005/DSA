# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recreate(self,root,val):
        while root:
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    return 
            elif root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return 

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            self.recreate(root,preorder[i])
        return  root
            

        