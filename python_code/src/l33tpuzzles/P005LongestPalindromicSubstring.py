from typing import List

"""
5. Longest Palindromic Substring


Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        """
        in the dynamic programming solution, keep a table, where row index is the first char of a substring,
        and col index is last char of a substring.

        idea is go through substrings of different sizes, starting with single char (size = 1), up to the entire string

        single chars are always palindrome, so dp[i][i] is always True

        double chars are palindrome when the chars are the same

        for substrings of length 3 and more, it is a palindrome IFF first and last char of substring match, AND the inner string is
        already a palindrome.  Since it has already iterated through substrings of smaller sizes, the DP table can already tell
        if the inner substring is a palindrome

    
        """
        slen = len(s)
        if slen == 0:
            return s
        
        dp: List[List[bool]] = [[False] * slen for _ in range(0, slen)]
        longest = 0
        longest_i = 0
        longest_j = 0

        for z in range(0, 2):
            for i in range(0, slen - z):
                j = i + z
                # print(f"z:{z}, i:{i}, j:{j}, s[i]:{s[i]}, s[j]:{s[j]}")
                if s[i] == s[j]:
                    dp[i][j] = True
                    if z + 1 > longest:
                        longest = z + 1
                        longest_i = i
                        longest_j = j
                #print(f"dp[{i}{j}]:{dp[i][j]}")
            

            
        for z in range(2, slen):
            for i in range(0, slen - z):
                j = i + z
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if z + 1 > longest:
                        longest = z + 1
                        longest_i = i
                        longest_j = j

        return s[longest_i:longest_j+1]
    

    def longestPalindromeCenterExpansion(self, s: str) -> str:
        """
        center expansion solution is start with a center, and expand outwards with left and right pointer to see if 
        the new substring is a panlindrome.

        center can be each single character for substrings of odd size, and can also be between two neiboring characters
        for substrings of even size
        """

        slen = len(s)

        longest = 1
        longest_left = 0
        longest_right = 0

        # odd 
        for i in range(0, slen):
            left = i - 1
            right = i + 1
            while left >=0 and right < slen:
                if s[left] == s[right]:
                    palin_size = right - left + 1
                    if palin_size > longest:
                        longest = palin_size
                        longest_left = left
                        longest_right = right
                    left = left - 1
                    right = right + 1
                else:
                    break
        
        # even
        for i in range(0, slen - 1):
            left = i
            right = i + 1
            while left >= 0 and right < slen:
                if s[left] == s[right]:
                    palin_size = right - left + 1
                    if palin_size > longest:
                        longest = palin_size
                        longest_left = left
                        longest_right = right
                    left = left - 1
                    right = right + 1
                else:
                    break

        return s[longest_left:longest_right+1]

    
    """
    also be aware of the Manacher's algorithm, which achieves O(n) instead of O(n^2).
    """


    
def main():
    solution = Solution()
    answer = solution.longestPalindromeCenterExpansion("babad")
    print(answer)
    print("done")

if __name__ == "__main__":
    main()
