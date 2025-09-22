# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        max_sum = 0
        result = []
        stack = [[root,0]] 
        while stack:
            length = len(stack)
            res1 = []
            for j in range(0,length): 
                node = stack.pop(0)
                if node[0].left:
                    stack.append([node[0].left, (2 * node[1]) + 1])
                    res1.append([node[0].left.val,(2 * node[1]) + 1]) 
                if node[0].right:
                    stack.append([node[0].right, (2 * node[1]) + 2])
                    res1.append([node[0].right.val,(2 * node[1]) + 2])   
            result.append(res1)
        result.pop()
        for i in range(len(result)-1,-1,-1):
            if len(result[i]) > 1:
                res2 = result[i][-1][1] - result[i][0][1] 
                if res2 > max_sum:
                    max_sum = res2
        print(result)
        return max_sum+1