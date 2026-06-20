from typing import List, Set, Tuple
"""
79. Word Search

Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

"""

class Solution:
    """
    recursion + backtrack

    first going through the board row by row, col by col until it finds the first letter of the target word.

    then it puts the current coordinate onto the visited set, and makes 4 calls to the recursive function. each call is for searching left, up, right, down. if any of the call comes back
    True, return True immediately without making the next call
    if none of the recursive call return True, then this cell is a dead end. Remove the coordinate from visited, and continue.


    for the recursive function call, pass in the index of the next letter to match in the target word, the visited set, the coordinate to check, plus info such as the board, the word, the number
    of rows and number of cols of the board

    if the passed in coordinate is beyond the boundary, or is already visited, return False

    if the letter at the coordinate matches the next letter of the word, and it is at the end of the word, return True; if not at end of the word, add current coordinate onto the visited set, and
    make 4 more recursive calls. Any call returning True should be returned True immediately

    if all 4 calls returned False, it is a dead end. remove the coordinate from visited, and return False
 
    
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited: Set[Tuple[int, int]] = set()
        row = len(board)
        col = len(board[0])
        wlen = len(word)

        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == word[0]:
                    if wlen == 1:
                        return True
                    else:
                        visited.add((r, c))
                        # search left
                        found = self.search(board, word, 1, r, c - 1, row, col, visited)
                        if found:
                            return True
                        # search up
                        found = self.search(board, word, 1, r - 1, c, row, col, visited)
                        if found:
                            return True

                        # search right
                        found = self.search(board, word, 1, r, c + 1, row, col, visited)
                        if found:
                            return True

                        # search down
                        found = self.search(board, word, 1, r + 1, c, row, col, visited)
                        if found:
                            return True
                        visited.remove((r, c))
        return False


    def search(self, board: List[List[str]], word: str, widx: int, r: int, c: int, row: int, col: int, visited: Set[Tuple[int, int]]) -> bool:
        if r < 0 or r >= row or c < 0 or c >= col or (r, c) in visited:
            return False
        l = board[r][c]
        if l == word[widx]:
            if widx == len(word) - 1:
                return True
            else:
                visited.add((r, c))
                # search left
                found = self.search(board, word, widx + 1, r, c - 1, row, col, visited)
                if found:
                    return True
                # search up
                found = self.search(board, word, widx + 1, r - 1, c, row, col, visited)
                if found:
                    return True

                # search right
                found = self.search(board, word, widx + 1, r, c + 1, row, col, visited)
                if found:
                    return True

                # search down
                found = self.search(board, word, widx + 1, r + 1, c, row, col, visited)
                if found:
                    return True
                visited.remove((r, c))
                return False
        else:
            return False
            
def main():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    word = "SEE"
    word = "ABCB"
    sol = Solution()
    print(sol.exist(board, word))

main()