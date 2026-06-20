from typing import List, Tuple
"""
85. Maximal RectangleSolved
Hard

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:

  1 | 0 | 1 | 0 | 0
 ---+---+---+---+---
  1 | 0 | 1 | 1 | 1
 ---+---+---+---+---
  1 | 1 | 1 | 1 | 1
 ---+---+---+---+---
  1 | 0 | 0 | 1 | 0


  1 | 0 | 1 | 0 | 0
 ---+---+---+---+---
  1 | 0 |.1.|.1.|.1.
 ---+---+---+---+---
  1 | 1 |.1.|.1.|.1.
 ---+---+---+---+---
  1 | 0 | 0 | 1 | 0



Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.

"""

class Solution:
    """
    The solution to this problem is built on top of the p084 largest rectangle in histogram.

    first convert the matrix into a number of histograms, where each row is a list of histogram bars. conversion: go through matrix row by row. for each cell, if matrix is "1", the bar height
    for this cell is the bar height of the cell above plus 1.  if the matrix cell is "0", then bar height resets to 0

    after having built the histogram, feed each row of the histogram to the largest rectangle in histograms, and track the max area. 


    https://www.youtube.com/watch?v=dAVF2NpC3j4
    
    """
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        max_area = 0
        histograms: List[List[int]] = [[0] * col for _ in range(0, row)]

        for c in range(0, col):
            histograms[0][c] = 1 if matrix[0][c] == "1" else 0

        for r in range(1, row):
            for c in range(0, col):
                if matrix[r][c] == "1":
                    histograms[r][c] = histograms[r-1][c] + 1
                else:
                    histograms[r][c] = 0

        print(f"histograms {histograms}")
        
        for r in range(0, row):
            area = self.largest_rec_in_histogram(histograms[r])
            max_area = max(area, max_area)

        return max_area

    
    def largest_rec_in_histogram(self, histo: List[int]) -> int:
        stack: List[Tuple[int, int]] = [(histo[0],0)]
    
        max_area = histo[0]

        for idx, h in enumerate(histo):
            start = idx
            while len(stack) > 0 and stack[-1][0] > h:
                bar = stack.pop()
                start = bar[1]
                area = bar[0] * (idx - bar[1])
                max_area = max(max_area, area)
            stack.append((h, start))

        while len(stack) > 0:
            bar = stack.pop()
            area = bar[0] * (len(histo) - bar[1])
            max_area = max(max_area, area)
            
        return max_area
        
def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["0"]]
    sol = Solution()
    print(sol.maximalRectangle(matrix))

main()