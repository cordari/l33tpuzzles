from typing import List, Set


class Solution:
    """
    37. Sudoku Solver

    Hard

    Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
    """


    """
    The solution is DFS (i.e. brute force).
      To make the solution a little dfficient, have 3 lists each containing 9 sets.  1 list represents each row; 1 each column; and 1 each block. The set holds the digits used for the perspective row/column/block
      Scan the board to initialize these sets

      Go row by row, then column by column, for each cell. If the cell is already filled in, recursive call for the next cell and return the outcome directly
      if the cell is not filled in, go through values "1" through "9". for each value,
        first check the sets for the corresponding row, column, and block. if the value is already in the set, go to the next value
        if the value is not in the set, update the board, and the sets with the value, and recursive call for the next cell
        if that recursive call returns successful, return the current function call with success
        otherwise, remove the value from the sets, and also clear the cell on the board, so the loop iteration can try the next possible value
      if it reaches outside of the loop, then it means none of 1-9 worked, so it must return False to backtrack

      at the beginning of this recursive function, one terminal condition to check is to ensure the row id doesn't exceed 8 (0 ~ 8). if it does, it means there is no possible solution for the board
      and should return False.

      But for this problem, it guarantees a solution, so it won't reach this condition in reality.

    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dig_in_rows: List[Set[str]] = [set() for _ in range(9)]
        dig_in_cols: List[Set[str]] = [set() for _ in range(9)]
        dig_in_blks: List[Set[str]] = [set() for _ in range(9)]


        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell != ".":
                    dig_in_rows[r].add(cell)
                    dig_in_cols[c].add(cell)
                    block_id = (r//3) * 3 + c//3
                    dig_in_blks[block_id].add(cell)

        self.solve(board, dig_in_rows, dig_in_cols, dig_in_blks, 0, 0)



    def solve(self, board:List[List[str]], dir:List[Set[str]], dic:List[Set[str]], dib:List[Set[str]], r: int, c: int) -> bool:
        if r == 9:
            return False
        
        new_c = c + 1
        new_r = r
        if new_c == 9:
            new_c = 0
            new_r += 1
        if board[r][c] != '.':
            return self.solve(board, dir, dic, dib, new_r, new_c)
        
        bid = (r//3)*3 + c//3
        for cel in ["1","2","3","4","5","6","7","8","9"]:
            if cel in dir[r] or cel in dic[c] or cel in dib[bid]:
               continue

            dir[r].add(cel)
            dic[c].add(cel)
            dib[bid].add(cel)
            board[r][c] = cel
            result = self.solve(board, dir, dic, dib, new_r, new_c)
            if result == True:
                return True
            dir[r].remove(cel)
            dic[c].remove(cel)
            dib[bid].remove(cel)
            board[r][c] = "."          
        return False

def main():
    input = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    sol = Solution()
    sol.solveSudoku(input)

    print(input)

        
if __name__ == "__main__":
    main()