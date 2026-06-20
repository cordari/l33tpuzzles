from typing import List
"""

51. N-Queens

Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

|   | Q |   |   |             |   |   | Q |   |
----+---+---+----             ----+---+---+----
|   |   |   | Q |             | Q |   |   |   |
----+---+---+----             ----+---+---+----
| Q |   |   |   |             |   |   |   | Q |
----+---+---+----             ----+---+---+----
|   |   | Q |   |             |   | Q |   |   |

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
"""

class Solution:
    """
    using recursion and backtrack. each recursive call is for 1 row since no two queens can be placed on the same row. when consider a position, check vertically, upper-left to lower-right diagnal, and upper-right
    to lower-left diagnal to make sure there isn't another queen.  through the call, keep a list that tracks the column position of each row. when it has collected N elements, copy of the list and add to the overall
    solutions list.  then pop the last element, either after added to the solutions list, or after a recursive call comes back, so it can check the next position.

    the final step before returning is the convert the solutions list to the required format with dots and Q.
    
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans: List[List[str]] = []
        track: List[int] = []
        board: List[List[bool]] = [[False] * n for _ in range(0, n)]

        self.q_helper(board, 0, track, n, ans)

        return ans

    def q_helper(self, board: List[List[bool]], row: int, track: List[int], n: int, ans: List[List[str]]):
        for i in range(0, n):
            # check column
            has_queen = False
            for r in range(0, row):
                if board[r][i]:
                    has_queen = True
                    break
            # check top left to bottom right diagnal
            if not has_queen:
                # go from here to upper left
                c = i - 1
                for j in range(row - 1, -1, -1):
                    if c >= 0 and c < n:
                        if board[j][c]:
                            has_queen = True
                            break
                    else:
                        break
                    c = c - 1
                
            if not has_queen:
                # go from here to bottom right
                c = i + 1
                for j  in range(row + 1, n):
                    if c >= 0 and c < n:
                        if board[j][c]:
                            has_queen = True
                            break
                    else:
                        break
                    c = c + 1    
                    
            # check top right to bottom left diagnal
            if not has_queen:
                # go from here to upper right
                c = i + 1
                for j in range(row - 1, -1, -1):
                    if c >= 0 and c < n:
                        if board[j][c]:
                            has_queen = True
                            break
                    else:
                        break
                    c = c + 1

            if not has_queen:
                # go from here to lower left
                c = i - 1
                for j in range(row + 1, n):
                    if c >= 0 and c < n:
                        if board[j][c]:
                            has_queen = True
                            break
                    else:
                        break
                    c = c - 1

            if not has_queen:
                board[row][i] = True
                track.append(i)
                if row == n - 1:
                    answer = []
                    for t in track:
                        token = ""
                        for x in range(0, t):
                            token += "."
                        token += "Q"
                        for x in range(t + 1, n):
                            token += "."
                        answer.append(token)
                    ans.append(answer)
                else:
                    self.q_helper(board, row + 1, track, n, ans)
                track.pop()
                board[row][i] = False



def main():
    sol = Solution()
    print(sol.solveNQueens(4))

if __name__ == "__main__":
    main()