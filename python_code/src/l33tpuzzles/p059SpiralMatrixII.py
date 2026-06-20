from typing import List
"""

59. Spiral Matrix II

Medium

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

  1 | 2 | 3
 ---+---+---
  8 | 9 | 4
 ---+---+---
  7 | 6 | 5

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""

class Solution:
    """
    same pattern as Sprial Matrix, where a reverse G pattern is used to traverse the cells in spiral 

    since this is generation with a nxn matrix, it is slightly easier as there won't be a 1xn strip. You can always check and stop when the number goes beyond n^2
    
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        output: List[List[int]] = [[0] * n for _ in range(0, n)]
        layers = (n + 1) // 2
        num = 1
        end = n*n

        for L in range(0, layers):
            # fill left -> right
            if num <= end:
                row = L
                start_c = L
                end_c = n - 1 - L
                num = self.fill_left_to_right(output, row, start_c, end_c, num, end)
            else:
                break

            # file top -> bottom
            if num <= end:
                col = n - 1 - L
                start_r = L + 1
                end_r = n - 1 - L
                num = self.fill_top_to_bottom(output, col, start_r, end_r, num, end)
            else:
                break

            # fill right -> left
            if num <= end:
                row = n - 1 - L
                start_c = n - 1 - 1 -L
                end_c = L
                num = self.fill_right_to_left(output, row, start_c, end_c, num, end)
            else: 
                break

            # fill bottom -> top
            if num <= end:
                col = L
                start_r = n - 1 - 1 - L
                end_r = L + 1
                num = self.fill_bottom_to_top(output, col, start_r, end_r, num, end)
            else: 
                break

        return output



    def fill_left_to_right(self, output: List[List[int]], row: int, start_c: int, end_c: int, num: int, end: int) -> int:
        for i in range(start_c, end_c + 1):
            output[row][i] = num
            num += 1
            if num > end:
                break
        return num

    def fill_top_to_bottom(self, output: List[List[int]], col: int, start_r: int, end_r: int, num: int, end: int) -> int:
        for i in range(start_r, end_r + 1):
            output[i][col] = num
            num += 1
            if num > end:
                break
        return num
    
    def fill_right_to_left(self, output: List[List[int]], row: int, start_c: int, end_c: int, num: int, end: int) -> int:
        for i in range(start_c, end_c - 1, -1):
            output[row][i] = num
            num += 1
            if num > end:
                break
        return num
    
    def fill_bottom_to_top(self, output: List[List[int]], col: int, start_r: int, end_r: int, num: int, end: int) -> int:
        for i in range(start_r, end_r - 1, -1):
            output[i][col] = num
            num += 1
            if num > end:
                break
        
        return num
    
def main():
    sol = Solution()
    print(sol.generateMatrix(4))

if __name__ == "__main__":
    main()
