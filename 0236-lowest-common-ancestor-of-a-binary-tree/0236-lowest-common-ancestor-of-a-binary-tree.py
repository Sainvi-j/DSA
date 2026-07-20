# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque([root])
        par = {root: None}

        while queue:
            if p in par and q in par:
                break

            node = queue.popleft()

            if node.left:
                par[node.left] = node
                queue.append(node.left)

            if node.right:
                par[node.right] = node
                queue.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = par[p]

        while q:
            if q in ancestors:
                return q
            q = par[q]

        return None