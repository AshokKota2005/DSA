# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if not p or not q:
            return False
        stack1 = [p]
        result1 = []
        result2 = []
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            result1.append(node1.val)
            node2 = stack2.pop()
            result2.append(node2.val)
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
                print("A")
            elif not node1.right and node2.right:
                print("B")
                return False
            elif node1.right and not node2.right:
                print("C")
                return False
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif not node1.left and node2.left:
                print("D")
                return False
            elif node1.left and not node2.left:
                print("E")
                return False 

        print("ddv")
        if result1 == result2:
            return True
        else:
            print("G")
            return False 
            



        