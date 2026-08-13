class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        from typing import List

class Node:
    __slots__ = ("prefLen", "sufLen", "best", "leftChar", "rightChar")
    def __init__(self, prefLen=0, sufLen=0, best=0, leftChar='', rightChar=''):
        self.prefLen = prefLen
        self.sufLen = sufLen
        self.best = best
        self.leftChar = leftChar
        self.rightChar = rightChar

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        tree = [Node() for _ in range(4 * n)]

        def merge(left, right, leftLen, rightLen):
            node = Node()
            node.leftChar = left.leftChar
            node.rightChar = right.rightChar

            if left.prefLen == leftLen and left.rightChar == right.leftChar:
                node.prefLen = left.prefLen + right.prefLen
            else:
                node.prefLen = left.prefLen

            if right.sufLen == rightLen and right.leftChar == left.rightChar:
                node.sufLen = right.sufLen + left.sufLen
            else:
                node.sufLen = right.sufLen

            bridge = 0
            if left.rightChar == right.leftChar:
                bridge = left.sufLen + right.prefLen
            node.best = max(left.best, right.best, bridge)
            return node

        def build(idx, l, r):
            if l == r:
                tree[idx] = Node(1, 1, 1, s[l], s[l])
                return
            mid = (l + r) // 2
            build(2*idx, l, mid)
            build(2*idx+1, mid+1, r)
            tree[idx] = merge(tree[2*idx], tree[2*idx+1], mid - l + 1, r - mid)

        def update(idx, l, r, pos, ch):
            if l == r:
                tree[idx] = Node(1, 1, 1, ch, ch)
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(2*idx, l, mid, pos, ch)
            else:
                update(2*idx+1, mid+1, r, pos, ch)
            tree[idx] = merge(tree[2*idx], tree[2*idx+1], mid - l + 1, r - mid)

        build(1, 0, n - 1)

        result = []
        for ch, pos in zip(queryCharacters, queryIndices):
            s[pos] = ch
            update(1, 0, n - 1, pos, ch)
            result.append(tree[1].best)
        return result