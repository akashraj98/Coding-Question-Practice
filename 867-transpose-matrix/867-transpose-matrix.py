class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)    # row
        n = len(matrix[0]) #col
        if m==n:
            for i in range(m):
                for j in range(i):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            return matrix
        else:
            # make aux matrix of size n*m
            auxMatrix = [[0]*m for _ in range(n)]
            # Traverse primary array
            for i in range(m):
                for j in range(n):
                    auxMatrix[j][i]=matrix[i][j]
            return auxMatrix