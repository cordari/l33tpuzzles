from typing import List
"""
73. Set Matrix Zeroes

Medium

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

  1 | 1 | 1            1 | 0 | 1 
 ---+---+---          ---+---+---
  1 | 0 | 1     ==>    0 | 0 | 0
 ---+---+---          ---+---+---
  1 | 1 | 1            1 | 0 | 1

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]


Example 2:

   0 | 1 | 2 | 0            0 | 0 | 0 | 0 
  ---+---+---+---          ---+---+---+---
   3 | 4 | 5 | 2     ==>    0 | 4 | 5 | 0
  ---+---+---+---          ---+---+---+---
   1 | 3 | 1 | 5            0 | 3 | 1 | 0

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

class Solution:
    """
    the problem asks for O(1) space, so we cannot use additional arrays to track the rows and columns that need to be zeroed out.

    The idea is to use the matrix itself. when matrix[r][c] is 0, place 0 as a marker at matrix[0][c] and at matrix[r][0] to indicate the column c and row r need to be zeroed out.

    This works fine except for matrix[0][0], where first row and first column markers overlap. If matrix[0][0] == 0, we cannot tell if it means to zero out only the first row, or only
    the first column, or both. So we need to introduce 2 additional boolean variables, first row zero, and first col zero, which are still under O(1).

    going through the matrix to find 0's. if the cell involves first row or/and first column, set the corresponding booleans; if the cell is not first row or first column, set their
    first row and first column cell to 0

    check from row 1 to rest; if first cell of each row is 0, zero out the entire row

    check from col 1 to rest; if first cell of each col is 0, zero out the entire column

    finally, if first row zero is true, zero out the first row; and if first col zero is true, zero out the first col. 
    
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False

        row = len(matrix)
        col = len(matrix[0])

        for r in range(0, row):
            for c in range(0, col):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_zero = True
                    if c == 0:
                        first_col_zero = True
                    if r > 0 and c > 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        for r in range(1, row):
            if matrix[r][0] == 0:
                for c in range(1, col):
                    matrix[r][c] = 0

        for c in range(1, col):
            if matrix[0][c] == 0:
                for r in range(1, row):
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(0, col):
                matrix[0][c] = 0

        if first_col_zero:
            for r in range(0, row):
                matrix[r][0] = 0
