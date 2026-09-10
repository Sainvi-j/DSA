# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if node is None:
                return (0,0)
            
            Lsum,Lsize = dfs(node.left)
            Rsum,Rsize = dfs(node.right)

            Tsum = Lsum + Rsum + node.val
            Tsize = Lsize + Rsize + 1

            if Tsum // Tsize == node.val:
                count += 1
            
            return (Tsum, Tsize)

        dfs(root)
        return count