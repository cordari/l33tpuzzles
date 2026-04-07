"""
10. Regular Expression Matching


Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
Return a boolean indicating whether the matching covers the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

"""
few of the best YT videos explaining this:

https://www.youtube.com/watch?v=nVi5v7rVbmA

https://www.youtube.com/watch?v=l3hda49XcDE

top-down DP is more intuitive than a bottom-up DP. top-down goes from the starting of both string and pattern to the end;
where as the bottom-up goes from the end, which is harder to understand when you are having trouble understanind the algorithm.


for the DP solution, the rows represent the substring LENGTH of the string from beginning to the current size; and columns represent
the substring LENGTH of the pattern from beginning to the current size.  True at [m][n] means the string substring of length m
match the pattern substring of length n; False otherwise.

therefore if the string is of length m, the DP should have m+1 rows to account for 0-length substring at the beginning. Same
goes for pattern string of length n, DP should have n+1 columns

the idea is check string char at length m and pattern char at length n:
1. if char at m equals pattern char at n, or if the pattern char at n is ".", then dp[m][n] would be True IFF dp[m-1][n-1] is True.
   which means if the substring without char at m, and pattern substring without char at n are also matching, then having char at m and
   pattern char at n matching also matches

2. if pattern char at n is a "*", then it can have 2 choices - matching status at [m][n] is True if any of the choice is True

  2A. X* matches 0 chars from the string, where X is pattern char at n-1. Then we can think of the pattern as if X* was never in
  the pattern, but it didn't consume the current string char at m, so the matching status would depend on if the string substring
  with char at m matches pattern substring with char at n-2 (before X*), i.e. dp[m][j-2]
  
  2B. X* matches 1 or more chars from the string. then mathcing status would depend on if the string char at m matching pattern 
      char at n-1, AND if string substring with char at m-1 matches pattern substring including the pattern char at n (i.e *),
      i.e. dp[m-1][n] matches. Why do we need to check if the match happens at the previous char in string? Because the X* is considered
      active (not consumed) in this maching 1 or more case, and we want to backtrack to see if it matched more than once. 

caution: can only initialize dp[0][0] to True for empty string matching empty string pattern, and initialize the rest of the first
column to false for non-empty chara matching empty string pattern.  Cannot initialize first row to False, think of the case: does empty-string
match the pattern "a*"?
        
"""
from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen = len(s)
        plen = len(p)

        dp: List[List[bool]] = [[False] * (plen + 1) for _ in range(0, slen + 1)]

        # initialize empty string to empty pattern string match to True
        dp[0][0] = True

        # initialize non-empty character matching empty string pattern to False
        for i in range(1, slen + 1):
            dp[i][0] = False

        for i in range(0, slen + 1):
            for j in range(1, plen + 1):
                s_idx = i - 1
                p_idx = j - 1

                s_char = s[s_idx]
                p_char = p[p_idx]

                print(f"s[{s_idx}]: {s_char}, p[{p_idx}]: {p_char}")
                self.print_bool_grid(dp)

                if s_char == p_char or p_char == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p_char == '*':
                    dp[i][j] = dp[i][j-2] or ((s_char == p[p_idx-1] or p[p_idx-1] == ".") and dp[i-1][j])
                    # print(f"s_char: {s_char}")
                    # print(f"p_char - 1: {p[p_idx - 1]}")
                else:
                    dp[i][j] = False

        return dp[slen][plen]
    
    def print_bool_grid(self, grid: list[list[bool]]) -> None:
        for row in grid:
            print(" ".join("1" if cell else "0" for cell in row))
    
def main():
    sol = Solution()
    print(sol.isMatch("aaa", "a"))

if __name__ == "__main__":
    main()
