"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

"""
algorithm is keeping a left and a right pointer. left at 0 initially with right moving to the right.
for each character the right is at, check if that character was already seen. If already seen, find its
position, if the position is greater than the left pointer, move the left pointer to one after that seen
position, and update the map of the character with the new position (where right is);  if the position
was less than the left pointer, just ignore it, because that position was a left-over (since we don't actively
remove character and index from parts that's outside of the current longest substring).  Then everytime track
the length and keep the longest length seen.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # does the unnecessary work of removing the entries from the dict
        #
        # if len(s) < 2:
        #     return len(s)
        
        # seen_chars_pos: dict[str, int] = {s[0]: 0}

        # left = 0
        # right = 1
        # longest = 1
        # curr_length = 1

        # while right < len(s):
        #     curr = s[right]
        #     if curr in seen_chars_pos:
        #         longest = longest if longest > curr_length else curr_length
        #         new_left = seen_chars_pos[curr] + 1
        #         for i in range(left, new_left):
        #             seen_chars_pos.pop(s[i])
        #         left = new_left
        #         curr_length = right - left + 1
        #     else:
        #         curr_length = curr_length + 1

        #     seen_chars_pos[curr] = right
        #     right = right + 1

        # longest = longest if longest > curr_length else curr_length
        # return longest

        if len(s) < 2:
            return len(s)
        
        seen_chars_pos: dict[str, int] = {s[0]: 0}

        left = 0
        longest = 1

        for right in range(1, len(s)):
            curr_char = s[right]
            if curr_char in seen_chars_pos and seen_chars_pos[curr_char] >= left:
                left = seen_chars_pos[curr_char] + 1
            
            seen_chars_pos[curr_char] = right

            longest = max(longest, right - left + 1)

        return longest

    

