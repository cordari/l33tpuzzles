"""
62. Unique Paths

Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:

 | S |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   |   |
 +---+---+---+---+---+---+---+
 |   |   |   |   |   |   | F |

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100

"""

from typing import List


class Solution:
    """
    This is a DP algorithm. Because the robot can only go right or go down, for each cell at [x, y], the number of paths to get there is the number of paths to get
    to the cell above it, i.e [x-1, y], plus number of paths to get to the cell left of it, i.e [x, y - 1].
    for the top row there is only 1 way to get to each cell, i.e. moving right; same for the left most column, which is moving down.
    
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[List[int]] = [[0] * n for _ in range(0, m)]

        # initialize path count for top row, to right of start. there is only 1 path to get to each cell in top row
        for i in range(0, n):
            dp[0][i] = 1

        # initialize path count for left column, below of start, there is only 1 path to get to each cell in left column
        for i in range(0, m):
            dp[i][0] = 1


        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
    
def main():
    sol = Solution()
    print(sol.uniquePaths(3, 2))

if __name__ == "__main__":
    main()
