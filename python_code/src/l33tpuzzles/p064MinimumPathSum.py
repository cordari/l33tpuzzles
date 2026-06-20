from typing import List

"""
64. Minimum Path Sum

Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

"""
class Solution:
    """
    DP algorithm. DP[x][y] is the minimum path sum to reach grid[x][y]
    1. initialize DP[0][0] with grid[0][0]
    2. initialize top row of DP by adding DP of the cell left of it with the number in current cell
    3. initialize left column of DP by adding DP of the cell above it with the number in current cell
    4. for rest of the cells, DP is the smaller between the DP left of it and DP above it, plus the number in current cell
    
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp: List[List[int]] = [[999] * n for _ in range(0, m)]

        dp[0][0] = grid[0][0]

        for c in range(1, n):
            dp[0][c] = dp[0][c-1] + grid[0][c]

        for r in range(1, m):
            dp[r][0] = dp[r-1][0] + grid[r][0]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])

        return dp[m-1][n-1]
    
def main():
    sol = Solution()
    print(sol.minPathSum([[1,2,3],[4,5,6]]))

if __name__ == "__main__":
    main()
        