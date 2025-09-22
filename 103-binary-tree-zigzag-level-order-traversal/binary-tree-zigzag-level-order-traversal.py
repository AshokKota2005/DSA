# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        result = []
        a = -1
        while stack:
            length = len(stack)
            res = []
            a += 1
            for j in range(0,length):
                node = stack.pop(0)
                res.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right) 
            if a%2 == 0:
                result.append(res)
            else:
                result.append(res[::-1])
        return result