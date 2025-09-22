# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        stack = []
        self.result = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            self.result.append(current.val)
            current = current.right

    def next(self) -> int:
        node = self.result[0]
        self.result.pop(0)
        return node
        
    def hasNext(self) -> bool:
        if self.result:
            return True
        else:
            return False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()