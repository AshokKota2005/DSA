# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        result = []
        ans = inf
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        for i in range(0,len(result)-1):
            for j in range(i+1,len(result)):
                if abs(result[i] - result[j]) < ans:
                    ans = abs(result[i] - result[j])
        return ans  
        