# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.nodes = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inOrderTraversal(root)
        return (self.nodes == sorted(self.nodes) and len(self.nodes) == len(set(self.nodes)))
    def inOrderTraversal(self, root) -> None:
        if not root:
            return None
        
        self.inOrderTraversal(root.left)
        self.nodes.append(root.val)
        self.inOrderTraversal(root.right)

        return None

