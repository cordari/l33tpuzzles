"""
44. Wildcard Matching
Solved
Hard
Topics
premium lock icon
Companies
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.

"""

from typing import List


class Solution:
    """
    video: https://www.youtube.com/watch?v=7SHV_QfVROE

    this is similar to leetcode p010 Regular Expression Matching, but slightly easier because the wild card is independent of the pattern char before it.

    using a top-down approach (going from start to end), with dynamic programming. for a string of size M and pattern of size N, DP table is (M+1) x (N+1) to account for
      the empty strings at the beginning for both string and pattern string.  DP[x][y] holds whether size x substring of the string matches size y substring of the pattern string.

    DP[0][0] would be True because empty string matches empty string

    DP[i][0] (where i != 0, rest of the first column) would be False because non-empty string doesn't match empty pattern string

    DP[0][j] where j != 0, initialize the first row. if not *, DP is false; if is *, DP = left of DP

    for each string char at m-1, and pattern char at n-1: (-1 because of 0-based indices)
    if pattern char is not a matcher char and matches string char, then DP[m][n] = DP[m-1][n-1]. meaning if the current string char equals current pattern char, we pretend these chars are not there, does the
       string without the current char match the pattern without the current pattern char.

    if pattern char is ? (single char matcher), and if string has a char (i.e. string length hasn't run out), DP[m][n] = DP[m-1][n-1]. same as above, pretend the chars don't exist, does the string without
       the current char match the pattern without current pattern char. (don't think we need to special handle if string runs out of a char because DP automatically takes care of that)

    if pattern char is * (wildcard matcher), then DP[m][n] = DP[m][n-1] OR DP[m-1][n]. DP[m][n-1] (i.e. left) means we think the * is matching nothing, does the string with current char match pattern string
       without the * char?  DP[m][n-1] (i.e above) means we think the current string char is consumed by the *, and does the string without the current char match the pattern with the * char

    the one part that is tripping my brain a little (same with regular expression matching) is how I keep thinking the above cases don't capture when the current string char is the starting matching char for *,
      but it seems the "above" case would take care of it, because the * matches empty, so if string without current char matches pattern without current pattern char, then adding a * to the pattern would also
      match the string without current char, and then adding the current char would also match. 

    """
    def isMatch(self, s: str, p: str) -> bool:
        dp: List[List[bool]] = [[False] * (len(p) + 1) for _ in range(0, len(s) + 1)]  # remember the len(x) + 1 because we need to accomodate the empty string

        dp[0][0] = True # empty string matches empty pattern string

        for r in range(1, len(s) + 1): # initialize the rest of the first column to False as empty pattern string won't match non-empty string
            dp[r][0] = False

        # initialize rest of first row
        for c in range(1, len(p) + 1):
            p_idx = c - 1
            p_char = p[p_idx]
            if p_char != "*":
                dp[0][c] = False
            else:
                dp[0][c] = dp[0][c-1] # no above case, only left cse


        for s_idx in range(0, len(s)):
            row_idx = s_idx + 1
            s_char = s[s_idx]
            for p_idx in range(0, len(p)):
                col_idx = p_idx + 1
                p_char = p[p_idx]
                if p_char != "*":
                    if p_char == "?" or p_char == s_char:
                        top_left = False
                        if row_idx - 1 >= 0 and col_idx - 1 >= 0:
                            top_left = dp[row_idx - 1][col_idx - 1]
                        dp[row_idx][col_idx] = top_left
                else:
                    left = False
                    above = False
                    if col_idx - 1 >= 0:
                        left = dp[row_idx][col_idx - 1]
                    if row_idx - 1 >= 0:
                        above = dp[row_idx - 1][col_idx]

                    dp[row_idx][col_idx] = left or above

        return dp[len(s)][len(p)]

def main():
    sol = Solution()
    print(sol.isMatch("aa", "aaa"))

if __name__ == "__main__":
    main()
