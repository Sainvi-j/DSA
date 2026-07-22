# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        n = len(nums)
        mid = n//2
        root = TreeNode(nums[mid])
        
        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n-1))

        while q:
            par, left, right = q.popleft()
            if left <= right:
                mid = (left+right)//2
                child = TreeNode(nums[mid])
                if nums[mid] < par.val:
                    par.left = child
                else:
                    par.right = child
                q.append((child, left, mid-1))
                q.append((child, mid+1, right))
        return root