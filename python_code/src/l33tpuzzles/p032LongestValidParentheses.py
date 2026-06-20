"""
32. Longest Valid Parentheses

Hard

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""

from typing import List


class Solution:
    """
    There are 2 solution algorithms.  1 uses stack; the other uses DP.

    The stack algorithm first

    for each character at index i, i.e. s[i]
      if s[i] = "(", push i onto stack.
      else if s[i] = ")", peek the top of the stack
        if the stack is empty, there is nothing to match it, push i onto stack. This i establishes the boundary of the latest invalid substring
        else
          if the top points to ")", there is no "(" matching the current ")", push i onto stack. This i establishes the boundary of the latest invalid substring
          else if the top points to "(", then the current ")" found a match, and this pair is valid. Pop the top first, then check:
            if the stack is empty, meaning it's a valid substring all the way from beginning, calculate the current length = i + 1, and compare the new length with prev max-length
            else calculate the current length = i - current top of stack. this is the distance between the lastest invalid boundary to i, and compare the current length with prev max-length

            (optimization: notice how the calculation of the current valid substring length varies depending on if the stack is empty or not. To not having to check this condition,
             we can initialize the stack wtih a "-1", so stack will never be empty, and length is always i - current top of stack.  Then the condition for push ")" index onto stack becomes
              if the top of the stack is -1, or top of stack is ")" )
              
    
    """
    def longestValidParentheses(self, s: str) -> int:
        stack: List[int] = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else: # char is ")""
                peek = stack[-1]
                if peek != -1 and s[peek] == "(":
                    stack.pop()
                    new_len = i - stack[-1]
                    max_len = max(max_len, new_len)
                else:
                    stack.append(i)
        return max_len
    

    """
    The DP algorithm

    dp[i] is the length of the longest valid substring ending at index i

    if char at i is "(", dp[i] = 0 because open paren is not valid
    if char at i is ")", then
      if char at i - 1 is "(", then it matches a valid pair. since dp[i-1] is always 0 (due to "(" never valid), we use dp[i-2] get the valid substring length from before, and then + 2, i.e. 
              dp[i] = dp[i - 2] + 2
      else char i - 1 is ")", then we don't know if that ")" closes a valid substring or not. So we use dp[i-1] to get the length of the valid substring at that ")", and we want to exam the
              char right before the valid substring ending at that ")" (however long it might be, could be 0 if that ")" is invalid). Designating the index of the char right before the valid
              substring as j.
          if the char at j is "(", then it matches with the ")" at i and is valid, so we know from j to i the substring is valid, but we also want to know what the length of valid substring
              is for the substring before j, in case j to i is a continuation of a valid substring, so we check dp[j - 1] and add that to the length of the valid substring from j to i,
              so dp[i] = dp[i-1] + 2 + dp[j-1].
          otherwise, dp[i] = 0

    keep a max_len to track the largest dp value  

    """
    def longestValidParentheses_dp(self, s: str) -> int:
        dp: List[int] = [0] * len(s)
        max_len = 0

        for i, c in enumerate(s):
            if c == "(":
                dp[i] = 0
            else:
                prev = i - 1
                if prev < 0: # at start of string, no previous char
                    dp[i] = 0
                else:
                    pc = s[prev]
                    if pc == "(": # prev char matches curr char as a pair
                        one_before = i - 2 # index of the char before prev. if there is no char before prev (start of string), len would be 2; otherwise, len would be the longest length at one before prev + 2
                        dp[i] = 2 if one_before < 0 else dp[one_before] + 2
                        max_len = max(max_len, dp[i])
                    else: # prev char was ")", need to check the character before the longest valid substring that ends with that prev char of ")"
                        idx_before_valid = i - dp[prev] - 1
                        if idx_before_valid < 0 or s[idx_before_valid] != "(": # invalid, either there is no character before the latest longest valid string, or the character is not "(", meaning it doesn't match the current ")" at i
                            dp[i] = 0
                        else:
                            prev_valid_idx = idx_before_valid - 1
                            prev_len = 0 if prev_valid_idx < 0 else dp[prev_valid_idx]
                            dp[i] = dp[i - 1] + 2 + prev_len
                            max_len = max(max_len, dp[i])
        return max_len
                    

        

def main():
    pattern = "(()"
    pattern = ")()())"
    pattern = ""
    pattern = ")))((("
    pattern = "()(())"
    pattern = "((((()))))"
    sol = Solution()
    print(sol.longestValidParentheses_dp(pattern))

if __name__ == "__main__":
    main()
