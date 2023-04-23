class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1  4  7
        2  5  8
        3  6  9
        """
        
        
        n = len(matrix) # rows
        m = len(matrix[0]) # col
        for i in range(1,n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()

            