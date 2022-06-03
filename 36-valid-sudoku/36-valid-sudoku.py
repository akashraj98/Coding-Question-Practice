class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in col[c] or
                    val in row[r] or 
                    val in squares[(r//3,c//3)]):  
                    return False
                
                col[c].add(val)
                row[r].add(val)
                squares[(r//3,c//3)].add(val) # using dictionary where 0,0 will
                                              # key for first box and so on
        
        return True
        