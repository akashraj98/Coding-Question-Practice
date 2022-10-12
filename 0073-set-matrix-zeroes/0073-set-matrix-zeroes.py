class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        x = y = 1
        for i in range(m):
            if matrix[i][0] == 0:
                y = 0
                break
        for j in range(n):
            if matrix[0][j] == 0:
                x = 0
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]== 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j] = 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        if x ==0:
            for j in range(n):
                matrix[0][j] = 0
        if y ==0:
            for i in range(m):
                matrix[i][0] = 0
        return matrix