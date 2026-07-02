class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        n = len(board)
        # checking rows
        for row in range(n):
            rowSet = set()
            for col in range(n):
                if not board[row][col].isdigit(): continue
                val = int(board[row][col])
                if val in rowSet:
                    is_valid = False
                    return is_valid
                else:
                    rowSet.add(val)
            if not is_valid:
                return False
                
        
        # checking colums
        for col in range(n):
            colSet = set()
            for row in range(n):
                if not board[row][col].isdigit() :continue
                val = int(board[row][col])
                if val in colSet:
                    is_valid = False
                    return False
                else:
                    colSet.add(val)
            if not is_valid:
                return False
        
        # checking boxes of 3x3
        for boxRow in range(0,9,3):
            for boxCol in range(0,9,3):
                boxSet = set()
                for i in range(boxRow, boxRow + 3):
                    for j in range(boxCol, boxCol + 3):
                        if not board[i][j].isdigit() : continue
                        val = int(board[i][j])
                        if val in boxSet:
                            is_valid = False
                            return False
                        else:
                            boxSet.add(val)
        
        if is_valid:
            return True

