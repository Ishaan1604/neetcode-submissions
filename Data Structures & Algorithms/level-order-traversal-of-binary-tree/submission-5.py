# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]
        res = []
        sett = set()
        while stack:
            node, depth = stack.pop()
            if depth not in sett:
                sett.add(depth)
                res.append([node.val])
            else:
                res[depth].append(node.val)
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        
        return res
