# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d_head = ListNode(-1, head)

        l_prev, currNode = d_head, head
        #setup
        for i in range(left-1):
            l_prev, currNode = currNode, currNode.next
        #tracking and reverse
        prev = None
        for i in range(right - left+1):
            next_p = currNode.next
            currNode.next = prev
            prev, currNode = currNode, next_p
        #updation
        l_prev.next.next = currNode
        l_prev.next = prev

        return d_head.next
        