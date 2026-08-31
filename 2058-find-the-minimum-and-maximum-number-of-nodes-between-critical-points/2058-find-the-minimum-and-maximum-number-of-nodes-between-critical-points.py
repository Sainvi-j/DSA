# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next

        idx = 1

        Icriti = -1
        Lcriti = -1
        minDist = float('inf')

        while curr.next:
            nxt_node = curr.next

            ismax = curr.val > prev.val and curr.val > nxt_node.val
            ismin = curr.val < prev.val and curr.val < nxt_node.val

            if ismax or ismin:
                if Lcriti == -1:
                    Icriti = idx
                else:
                    minDist = min(minDist, idx - Lcriti)

                Lcriti = idx

            prev = curr
            curr = nxt_node
            idx += 1
        
        if Icriti == -1 or Icriti == Lcriti:
            return [-1,-1]
        
        maxDist = Lcriti - Icriti

        return [minDist, maxDist]