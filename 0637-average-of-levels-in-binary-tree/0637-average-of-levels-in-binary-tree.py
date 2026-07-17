# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])

        res = []
        while queue:
            lvl=[]
            for i in range(len(queue)):
                node = queue.popleft()
                lvl.append(node.val)
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(sum(lvl)/len(lvl))
        return res
        