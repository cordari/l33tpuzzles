from typing import Dict, List

"""
52. N-Queens II

Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9

"""
class Solution:
    """
    same as N-Queen, except simpler as it doesn't need to return the board format. In this implementation, instead of using an nxn to track the actual board, I am using a dict to track the row and col position
    of each queen, dict[row] = col.  Also pass in a List of 1 element to increment the solution count
    
    """
    def totalNQueens(self, n: int) -> int:
        ans: List[int] = [0]
        existing: Dict[int, int] = {}
        self.nq_helper(0, n, existing, ans)

        return ans[0]

    def nq_helper(self, row: int, n: int, existing: Dict[int, int], ans: List[int]):
        for i in range(0, n):
            has_queen = False

            # check vertical
            for j in range(0, row):
                if j in existing and existing[j] == i:
                    has_queen = True
                    break

            # check top-left to lower-right:
            
            if not has_queen:
                # check here to top left
                col = i
                for j in range(row - 1, -1, -1):
                    col -= 1
                    if col >= 0:
                        if j in existing and existing[j] == col:
                            has_queen = True
                            break
            if not has_queen:
                # check here to lower right
                col = i
                for j in range(row + 1, n):
                    col += 1
                    if col < n:
                        if j in existing and existing[j] == col:
                            has_queen = True
                            break

            # check top-right to lower-left:
            if not has_queen:
                # check here to top right
                col = i
                for j in range(row - 1, -1, -1):
                    col += 1
                    if col < n:
                        if j in existing and existing[j] == col:
                            has_queen = True
                            break
            
            if not has_queen:
                # check here to lower left
                col = i
                for j in range(row + 1, n):
                    col -= 1
                    if col >= 0:
                        if j in existing and existing[j] == col:
                            has_queen = True
                            break

            if not has_queen:
                if row == n - 1:
                    ans[0] = ans[0] + 1
                else:
                    existing[row] = i
                    self.nq_helper(row + 1, n, existing, ans)
                    existing[row] = -1 # reset

def main():
    sol = Solution()
    print(sol.totalNQueens(5))

if __name__ == "__main__":
    main()
