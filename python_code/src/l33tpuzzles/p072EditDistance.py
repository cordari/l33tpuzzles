"""
72. Edit Distance

Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

"""

from typing import List


class Solution:
    """
    Edit distance is a classic DP problem.

    for intuition, let's say we want to convert "??c" -> "##x". There are 3 choices for changing the "c" to an "x":
    1. replace c with x, now solve smaller problem "??" -> "##"
    2. delete c from abc, now solve smaller problem "??" -> "##x"
    3. insert x in abc, it would become "??cx" -> "##x", which becomes smaller problem "??c" -> "##"

    of the 3 operation, you pick the smaller problem with the least cost, and the cost for current letter is 1 plus the least cost of smaller/prev problem

    and if the current letter from word1 and word2 are the same, then current letter doesn't incur cost, so you copy the cost of the smaller problem where both words are without their current matching letter

    DP[i][j] holds the minimal cost for word1 of length i to be converted to word2 of length j.

    DP would have m+1 rows and n+1 columns, where m and n are the lengths of word1 and word2, respectively

    DP[0][0] is the cost of converting empty string "" to empty string "", which is 0
    DP[0][c] is the cost of converting empty string "" to word2 of length c, so you have to do c inserts to produce length c, so dp[0][c] = c
    DP[r][0] is the cost of converting word1 of length r to empty "", so you have to do r removes to produce empty strings, so dp[r][0] = r

    then for the rest of the table at r, c:
    1. for a replace operation, the cost of smaller problem is from DP[r-1][c-1]
    2. for a delete operation, the cost of smaller problem is from DP[r-1][c]
    3. for a insert operation, the cost of smaller problem is from DP[r][c-1]

    and if the current letters match from both words, you copy from the DP of the words without their current letters, which is DP[r-1][c-1]

    
    """
    def minDistance(self, word1: str, word2: str) -> int:
        dp: List[List[int]] = [[float("inf")] * (len(word2) + 1) for _ in range(0, len(word1) + 1)]

        dp[0][0] = 0 # 0 edits needed to go from empty string to empty string

        for c in range(1, len(word2) + 1):  # when word1 is empty string, how many edits are needed to create a partial word2 of length c? c inserts
            dp[0][c] = c

        for r in range(1, len(word1) + 1): # when word2 is empty string, how many edits are needed to convert a partial word1 of length r to empty string (word2)? r removals
            dp[r][0] = r

        for r in range(1, len(word1) + 1):
            for c in range(1, len(word2) + 1):
                replace_cost = dp[r-1][c-1]

                remove_cost = dp[r-1][c]

                insert_cost = dp[r][c-1]

                prev_cost = min(replace_cost, min(remove_cost, insert_cost))

                if word1[r-1] != word2[c-1]:
                    dp[r][c] = 1 + prev_cost
                else:
                    dp[r][c] = dp[r-1][c-1]

        return dp[len(word1)][len(word2)]
    
def main():
    word1 = "aa"
    word2 = "a"
    sol = Solution()
    print(sol.minDistance(word1, word2))

main()