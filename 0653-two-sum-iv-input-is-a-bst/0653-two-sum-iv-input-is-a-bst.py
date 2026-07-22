# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque([root])
        num_set = set()

        while queue:
            node = queue.popleft()

            if (k - node.val) in num_set:
                return True
            else:
                num_set.add(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
        