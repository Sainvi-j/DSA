# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        par = None
        curr = root
        #Finding the node to del and parent
        while curr and curr.val != key:
            par = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        #if node not found end case
        if not curr:
            return root
        
        #case1 if node has no children
        if not curr.left and not curr.right:
            if not par:
                return None
            if par.left == curr:
                par.left = None
            else:
                par.right = None

        #case2 if node has 1 child
        elif not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right

            if not par:
                return child
            if par.left == curr:
                par.left = child
            else:
                par.right = child

        #case3 if node has 2 children    
        else:
            #find the smallest root in the subtree
            succ_par = curr
            succ = curr.right
            while succ.left:
                succ_par = succ
                succ = succ.left
            #copying
            curr.val = succ.val

            #deleting
            if succ_par.left == succ:
                succ_par.left = succ.right
            else:
                succ_par.right = succ.right
        return root


        