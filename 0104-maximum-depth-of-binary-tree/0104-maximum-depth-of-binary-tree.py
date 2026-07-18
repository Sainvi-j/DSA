# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue =  deque([(root, 1)])

        while queue:
            node, lvl = queue.popleft()
            if node.right:
                queue.append((node.right, lvl+1))
            if node.left:
                queue.append((node.left, lvl+1))
        return lvl