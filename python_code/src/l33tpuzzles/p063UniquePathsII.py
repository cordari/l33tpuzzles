from typing import List
"""
63. Unique Paths II

Medium

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

| S |   |   |
+---+---+---+  
|   | X |   |
+---+---+---+  
|   |   | F |


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:

| S | X |
+---+---+
|   | F |

Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""

class Solution:
    """
    similar to unique paths, use DP. Except you need to check against obstacleGrid. If cell [x,y] has obstacle, dp[x][y] = 0.
    also, cannot initialize top row and left column blindly as 1. instead, initialize dp[0][0] as 1 unless it has obstacle then it would be 0
    then for rest of top row, it would be the path count left of the cell, and for rest of left column, it would be path count of above the cell 
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp:List[List[int]] = [[0] * col for _ in range(0, row)]

        for r in range(0, row):
            for c in range(0, col):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    if r == 0 and c == 0:
                        dp[r][c] = 1
                    elif r == 0:
                        dp[r][c] = dp[r][c-1]
                    elif c == 0:
                        dp[r][c] = dp[r-1][c]
                    else:
                        dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[row-1][col-1]
    
def main():
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[1,0]]))

if __name__ == "__main__":
    main()