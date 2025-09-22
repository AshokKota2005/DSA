# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        result = []
        while stack:
            length = len(stack)
            res = []
            for i in range(length):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append('None')
                if node.right:
                    stack.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append('None')
            result.append(res)
        result = result[:-1]
        for i in range(0,len(result)):
            mid = len(result[i])//2
            part1 = result[i][:mid]
            part2 = result[i][mid:]
            part2 = part2[::-1]
            if part1 != part2:
                return False
        return True
                







