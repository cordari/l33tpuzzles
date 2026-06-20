from typing import List
"""
48. Rotate Image

Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:

1 | 2 | 3        7 | 4 | 1
--+---+--        --+---+--
4 | 5 | 6   =>   8 | 5 | 2
--+---+--        --+---+--
7 | 8 | 9        9 | 6 | 3

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


Example 2:

5 | 1 | 9 | 11              15| 13| 2 | 5
--+---+---+---              --+---+---+--
2 | 4 | 8 | 10              14| 3 | 4 | 1 
--+---+---+---     =>       --+---+---+--
13| 3 | 6 | 7               12| 6 | 8 | 9
--+---+---+---              --+---+---+---
15| 14| 12| 16              16| 7 | 10| 11


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    """
    Think in terms of layers, where each layer is like a square donut

    for each layer, think in terms of 4 strips:
    
               +---+ +--------------------+
               |   | |       UR           |
               |   | +--------------------+
               | U |                  +---+
               | L |                  |   |
               |   |                  |   |
               |   |                  | L |
               +---+                  | R |
               +--------------------+ |   |
               |       LL           | |   |
               +--------------------+ +---+    
    
    the idea is to cache 1 strip, and then copy a different strip into it, doing it 3 times, and then place the cached strip into the last one.

    my algorithm chooses to cache upper-left strip, and then move lower-left -> upper-left, and move lower-right into lower-left, and move upper-right into lower-right, and finally move
    the cached strip into upper right.

    N = number of rows/cols of original matrix

    LAYERS = (N + 1) // 2, because:
       1 x 1 matrix -> 1 layer
       2 x 2 matrix -> 1 layer
       3 x 3 matrix -> 2 layers
       4 x 4 matrix -> 2 layers
       5 x 5 matrix -> 3 layers
       6 x 6 matrix -> 3 layers
       ...

    use L to designate layer ID, from [0 ~ LAYERS - 1]

    for each layer, the number of elements in each side: SIZE_SIZE = N - 2 * L. Note a strip is a side minus 1 element

    use X to designate index, each side would have a row or a column index that varies from [0 ~ SIDE_SIZE - 1]

    use n to designate max index of original matrix, i.e. n = N - 1

                               __________________ (L, L + 1)
                               | 
                               v
    (L, L)             +---+ +--------------------+
         |---------->  |   | |       UR           |  <------- (L, n - L)
                       |   | +--------------------+
                       | U |                  +---+ 
                       | L |                  |   |  <------- (L + 1, n - L)
                       |   |                  |   |
          |--------->  |   |                  | L |
    (n - L - 1, L)     +---+                  | R |
                       +--------------------+ |   |
    (n - L, L) ------> |       LL           | |   |
                       +--------------------+ +---+    
                                          ^     ^
                                          |     |
               (n - L, n - L - 1)  _______|     |______ (n - L, n - L)
                       
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        n = N - 1 # last index is N - 1
        LAYERS = (N + 1) // 2
        

        for l in range(0, LAYERS):
            count = n - 2 * l
            if count < 1:
                break
            buffer: List[int] = [-1] * (count)
            # buffer upper left strip
            for i in range(0, count):
                buffer[i] = matrix[l+i][l]

            # move lower left strip to upper left
            for i in range(0, count):
                source_row = n - l
                source_col = l + i
                dest_row = l + i
                dest_col = l
                matrix[dest_row][dest_col] = matrix[source_row][source_col]

            # move lower right strip to lower left
            for i in range(0, count):
                source_row = n - l - i
                source_col = n - l
                dest_row = n - l
                dest_col = l + i
                matrix[dest_row][dest_col] = matrix[source_row][source_col]

            # move upper right strip to lower right
            for i in range(0, count):
                source_row = l
                source_col = l + 1 + i
                dest_row = l + 1 + i
                dest_col = n - l
                matrix[dest_row][dest_col] = matrix[source_row][source_col]

            # move the buffered strip into upper right
            for i in range(0, count):
                dest_row = l
                dest_col = n - l - i
                matrix[dest_row][dest_col] = buffer[i] 

def main():
    mat = [[1,2],[3,4]]
    sol = Solution()
    sol.rotate(mat)
    print(mat)

if __name__ == "__main__":
    main()

        