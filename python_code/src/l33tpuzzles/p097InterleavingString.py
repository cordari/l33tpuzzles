from typing import List
"""
97. Interleaving String

Medium

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:

[aabcc]       (dbbca)

[aa](dbbc)[bc](a)[c]

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

"""

class Solution:
    """
    DP problem. 

    first, return false if the lengths of s1 and s2 don't add up to s3

    initialize DP[0][0] = True, meaning s1 being empty string, and s2 being empty string, can always interleave into an empty string s3

    designate row of DP to be length of 1 of the strings (s2), and column of DP to be length of the other string (s1)

    the rest of first row means if s1 alone (with empty string s2) can interleave into s3.  if s1[r-1] == s3[r-1], then dp[r] = dp[r-1] else False. if the rth chars of s1 and s3 match, then
    dp of this position depends on if substring of s1 to (r-1)th char matches substring of s3 to (r-1)th char

    the rest of first column is similiar, i.e. if s2 alone (with emtpy string s1) can interleave into s3.

    for the rest of the DP table, DP[r][c] checks if the current char of s3 matches the latest char of s1 or matches the latest char of s2.  if it matches latest char of s1, then DP[r][c] is True
    only if the s3 substring without the current char is interleaved by s1 without the latest char and s2 substring so far.  if it matches latest char of s2, then DP[r][c] is True only if the s3
    substring without the current char is interleaved by s2 without the latest char and s1 substring so far, so the logic is

    DP[r][c] = (s1[c-1] == s3[r+c-1] AND DP[r][c-1])  OR (s2[r-1] == s3[r+c-1] AND DP[r-1][c])

    a BUGGY logic would be:

    if s1[c-1] == s3[r+c -1] OR s2[r-1] == s3[r+c-1]:
       DP[r][c] = DP[r][c-1] OR DP[r-1][c]
    else:
       DP[r][c] = False

    because this is saying, as long as the current char of s3 matches one of the latest chars of s1 or s2, then it is interleavable as long as the s3 without current char matches one of the substrings
    of s1 or s2 without its latest char.  this fails "aaa", "bbb" -> "bbbbbb"



    
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) - len(s1) - len(s2) != 0:
            return False
        
        dp: List[List[bool]] = [[False] * (len(s1) + 1) for _ in range(0, len(s2) + 1)]
        dp[0][0] = True

        for r in range(1, len(s2) + 1):
            s2_idx = r - 1
            s3_idx = r - 1
            if s2[s2_idx] == s3[s3_idx]:
                dp[r][0] = dp[r-1][0]
            else:
                dp[r][0] = False

        for c in range(1, len(s1) + 1):
            s1_idx = c - 1
            s3_idx = c - 1
            if s1[s1_idx] == s3[s3_idx]:
                dp[0][c] = dp[0][c - 1]
            else:
                dp[0][c] = False

        for r in range(1, len(s2) + 1):
            for c in range(1, len(s1) + 1):
                s2_idx = r - 1
                s1_idx = c - 1
                s3_idx = r + c - 1

                dp[r][c] = (s3[s3_idx] == s2[s2_idx] and dp[r - 1][c]) or (s3[s3_idx] == s1[s1_idx] and dp[r][c - 1])

        return dp[len(s2)][len(s1)]
    
def main():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    # s3 = "aadbbbaccc"

    # s1 = ""
    # s2 = ""
    # s3 = ""

    # s1 = "ab"
    # s2 = "bc"
    # s3 = "babc"

    # s1 = "aaa"
    # s2 = "bbb"
    # s3 = "bbbbbb"
    sol = Solution()

    print(sol.isInterleave(s1, s2, s3))

main()



