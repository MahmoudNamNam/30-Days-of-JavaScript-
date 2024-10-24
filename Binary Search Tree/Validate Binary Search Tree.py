from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True
        
        if not (low < root.val < high):
            return False
        
        return (self.isValidBST(root.left, low, root.val) and
                self.isValidBST(root.right, root.val, high))
