# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack = [[root, 0, 0]]
        d = {}
        while stack:
            length = len(stack)
            for j in range(length):
                node = stack.pop(0)
                if node[2] in d:
                    d[node[2]].append([node[1], node[0].val])  
                else:
                    d[node[2]] = [[node[1], node[0].val]]
                if node[0].left:
                    stack.append([node[0].left, node[1] + 1, node[2] - 1])
                if node[0].right:
                    stack.append([node[0].right, node[1] + 1, node[2] + 1])
        d = dict(sorted(d.items())) 
        print(d)  
        list1 = []
        for x in d:
            d[x].sort() 
            list1.append([val for _, val in d[x]]) 
        print(list1)  
        return list1

        