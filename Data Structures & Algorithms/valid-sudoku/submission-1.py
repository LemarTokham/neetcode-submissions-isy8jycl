class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row - If repeat within each row, return false
        rows = set() # O(1) lookup
        for i in range(len(board)):
            rows.clear()
            for j in range(len(board)):
                val = board[i][j]
                if val != '.': # skipping empty cells
                    if val not in rows: # if not full stop it must be a digit
                        rows.add(val)
                    else:
                        print("hit")
                        return False
                    
        # Check col
        cols = set()
        for i in range(len(board)):
            cols.clear()
            for j in range(len(board)):
                val = board[j][i]
                if val != '.':
                    if val not in cols: # if not full stop it must be a digit
                        cols.add(val)
                    else:
                        print("hit")
                        return False

        # 3x3 Board check
        count = 0
        box = set()
        i = 0
        j = 0 # col
        while i < len(board):
            print(i)

            if j > 8: # reset col once at end
                j = 0
                i += 3
                if i > 8:
                    break

            # loop through rows
            for k in range(i, i + 3):
                # print(i, j)
                val = board[j][k]
                if val != '.':
                    if val not in box:
                        box.add(val)
                    else:
                        print("hit")
                        return False

            count += 1
            if count == 3:
                box.clear() # reset box
                count = 0
                
            j += 1
        
        return True

