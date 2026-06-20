"""
91. Decode Ways

Medium

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

from typing import List


class Solution:
    """
    DP solution. 

    DP[i] means the number of decode ways for substring ending at ith character in the string. DP[0] is empty string, which = "1"

    for ith character, if the character is valid on its own, add DP[i-1]; if the character combined with the previous character are also valid, add DP[i-2] as well.

    note above I am using ith character, which is 1-based. when the index is 0-based, the corresponding DP index for that character is i + 1
    
    """
    def numDecodings(self, s: str) -> int:
        dp: List[int] = [0] * (len(s) + 1)  # dp = number of ways to intepret substring ending at ith character.  dp[0] is for empty string at the beginning

        dp[0] = 1 # empty string initializes to 1
        c = s[0]
        dp[1] = 0 if c == "0" else 1  # first character has 1 way to decode UNLESS it is a "0" which cannot be on its own

        for i in range(1, len(s)):
            c = s[i]
            if c == "0":
                if s[i - 1] >= "1" and s[i - 1] <= "2":
                    dp[i + 1] = dp[i - 1]
                else:
                    dp[i + 1] = 0
            elif c >= "1" and c <= "6":
                if s[i - 1] >= "1" and s[i - 1] <= "2":
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
            else: # c is 7 - 9
                if s[i - 1] == "1":
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]

        return dp[len(s)]
    
def main():
    str = "12"
    str = "226"
    str = "06"
    #str = "20"
    sol = Solution()

    print(sol.numDecodings(str))

main()       
       