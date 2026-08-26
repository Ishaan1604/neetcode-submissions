# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.inOrderTraversal(root)
        return self.nodes[k - 1]
    
    def inOrderTraversal(self, root) -> None:
        if root:
            self.inOrderTraversal(root.left)
            self.nodes.append(root.val)
            self.inOrderTraversal(root.right)
        
        return