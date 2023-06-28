class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # queen moves diagonally X and in same cell +
        # we start by placing queen at first pos 
        # and mork all the positions as slate
        # next we find all other pos queeen can be place and mark it as placed
        # Create a grid of n*n
        # remember only one queen can be placed in a row or column
        
        res = []
        board = [["."]*n for i in range(n)]
        def is_valid_pos(row, col):
            for i in range(n):
                if board[i][col] == "Q":
                    return False

            for j in range(n):
                if board[row][j] == "Q":
                    return False

            directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

            for dr, dc in directions:
                r = row
                c = col
                while 0 <= r < n and 0 <= c < n:
                    if board[r][c] == "Q":
                        return False
                    r += dr
                    c += dc

            return True
            
        def backtrack(col):
            if col == n:
                nboard = ["".join(row) for row in board]
                res.append(nboard)
                return
            for row in range(n):
                if is_valid_pos(row,col):
                    board[row][col] = "Q"
                    backtrack(col+1)
                    board[row][col] = "."
        
        backtrack(0)
        return res