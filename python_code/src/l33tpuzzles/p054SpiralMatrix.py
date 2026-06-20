from typing import List
"""
54. Spiral Matrix

Medium

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

"""

class Solution:
    """
     tackle layer by layer.  because the matrix is rectangular, the number of layers is determined by the shorter of the row count and the column count

     for each layer, do a reverse G, i.e.

     
         R = L, start_C = L, end_C = c_count - 1 - L
         +-------------------------+
         |         L -> R          |
         +-------------------------+
         +---+                 +---+
         | ^ |                 |   | C = c_count - 1 - L, start_R = L + 1, end_R = r_count - 1 - L
         | | |                 | T |
         +---+                 | | |
         +--------------------+| v |
         |        L  <-  R    || B |
         +--------------------++---+
        R = r_count - 1 - L, start_C = c_count - 2 - L, end_C = L

        left: C = L, start_R = r_count - 2 - L, end_R = L + 1

    
    there are edge cases when a layer is a mx1 or 1xn strip; which could end up being used for multiple directions.  One way to limit that is keep a min_r, max_r, min_c, max_c, and squeeze the rows and
    columns.  After L -> R, min_r increments by one; after T -> B, max_c decrements by one; after R -> L, max_r decrements by 1, and after B -> T, min_c increments by 1. And every time before processing
    1 direction, check the pinned row or pinned column is within the min and max


    """


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r_count = len(matrix)
        c_count = len(matrix[0])
        r_layer = (r_count + 1) // 2
        c_layer = (c_count + 1) // 2

        min_r = 0
        max_r = r_count - 1
        min_c = 0
        max_c = c_count - 1

        print(f"r_layer:{r_layer}, c_layer:{c_layer}")

        layer_count = min(r_layer, c_layer)

        output = []

        for L in range(0, layer_count):
            # top left -> right
            row = L
            start_c = L
            end_c = c_count - 1 - L
            print(f"end_c:{end_c}")
            if row >= min_r and row <= max_r:
                result = self.read_left_to_right(matrix, row, start_c, end_c)
                min_r += 1
                print(f"left to right: {result}")
                output.extend(result)

            # right top -> bottom
            col = c_count - 1 - L
            start_r = L + 1
            end_r = r_count - 1 - L
            if col >= min_c and col <= max_c:
                result = self.read_top_to_bottom(matrix, col, start_r, end_r)
                max_c -= 1
                print(f"top to bottom: {result}")
                output.extend(result)

            # bottom right -> left
            row = r_count - 1 - L
            start_c = c_count - 2 - L
            end_c = L
            print(f"bottom right -> left start_c: {start_c}, max_c: {max_c}, end_c: {end_c}, min_c: {min_c}")
            if row >= min_r and row <= max_r: # min_c <= start_c and start_c <= max_c and min_c <= end_c and end_c >= min_c:
                result = self.read_right_to_left(matrix, row, start_c, end_c)
                max_r -= 1
                print(f"right to left: {result}")
                output.extend(result)

            # left bottom -> top
            col = L
            start_r = r_count - 2 - L
            end_r = L + 1
            print(f"left bottom -> top start_r: {start_r}, min_r:{min_r}, end_r:{end_r}, max_r:{max_r}")
            if col >= min_c and col <= max_c: # and min_r <= start_r and start_r <= max_r and min_r <= end_r and end_r <= max_r:
                result = self.read_bottom_to_top(matrix, col, start_r, end_r)
                min_c += 1
                print(f"bottom to top: {result}")
                output.extend(result)

        return output




    def read_left_to_right(self, matrix: List[List[int]], row: int, start_c: int, end_c: int) -> List[int]:
        nums = []
        for c in range(start_c, end_c + 1):
            nums.append(matrix[row][c])
        return nums
    
    def read_top_to_bottom(self, matrix: List[List[int]], col: int, start_r: int, end_r: int) -> List[int]:
        nums = []
        for r in range(start_r, end_r + 1):
            nums.append(matrix[r][col])
        return nums
    
    def read_right_to_left(self, matrix: List[List[int]], row: int, start_c: int, end_c: int) -> List[int]:
        nums = []
        for c in range(start_c, end_c - 1, -1):
            nums.append(matrix[row][c])
        return nums
    
    def read_bottom_to_top(self, matrix: List[List[int]], col: int, start_r: int, end_r: int) -> List[int]:
        nums = []
        for r in range(start_r, end_r - 1, -1):
            nums.append(matrix[r][col])
        return nums
    
def main():
    matrix = [[1,2, 3],[4,5,6],[7,8,9], [10, 11, 12]]
    sol = Solution()
    print(sol.spiralOrder(matrix))

if __name__ == "__main__":
    main()
    