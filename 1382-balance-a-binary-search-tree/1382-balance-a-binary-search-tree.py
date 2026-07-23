# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Sorted Array
        nodes = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            nodes.append(curr.val)
            curr = curr.right
        
        #Sorted Array To BST
        def sortedArrayToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nodes[mid])
            
            node.left = sortedArrayToBST(left, mid - 1)
            node.right = sortedArrayToBST(mid + 1, right)
            
            return node

        return sortedArrayToBST(0, len(nodes) - 1)