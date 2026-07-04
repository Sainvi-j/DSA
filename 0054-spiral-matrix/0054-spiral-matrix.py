class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            #add the 1st row
            ret += (matrix.pop(0))
            #append the last elelment of all the list
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            #add reverse of the last row of the list
            if matrix:
                ret += (matrix.pop()[::-1])
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret