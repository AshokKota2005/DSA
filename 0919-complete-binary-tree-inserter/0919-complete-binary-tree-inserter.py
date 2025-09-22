# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
    def insert(self, val: int) -> int:
        current = self.root
        stack = [current]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            else:
                node.left = TreeNode(val)
                return node.val
            if node.right:
                stack.append(node.right)
            else:
                node.right = TreeNode(val) 
                return node.val 

    def get_root(self) -> Optional[TreeNode]:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()