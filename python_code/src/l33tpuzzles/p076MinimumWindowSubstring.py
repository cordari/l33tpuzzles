"""
76. Minimum Window Substring
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?

"""

from typing import Dict


class Solution:
    """
    sliding window problem
    1. build a "required" dictionary with required letter and frequency from the target word
    2. the number of keys in the dictionary is the "needed" count
    3. build a "tracker" dictionary to track required letter frequency of the source word, initially set them to 0
    4. set a formed counter to be 0. formed counter is a lighter weight way to check and tell if substring has met the target word requirement. when a letter frequency equals the required frequency, 
     increment the formed counter. when formed counter == needed, substring satisfies. without using this counter, we would have to check the dictionary every time
    5. when the formed counter is less than needed count, and window right pointer is not at the end, expand the window to the right. take a look at the character at the right boundary and update
      tracker if appropriate, and also increment formed counter if appropriate. if formed == needed, calculate the current window; if it is less than the known min window, update the window size, 
      update the window boundaries with current left and right value.  To make things easier, right can be initialized to -1, so we can always increment and check character
    6. when the formed counter equals needed count, we shrink the window by advancing the left boundary. before moving the left pointer, check the letter at the left, and decrement the letter frequency
      if appropriate, and also decrement formed counter if appropriate. advance left pointer.  if formed counter still equals needed, calculate window size, and if it is smaller, update window size,
      and set boundary to the current left and right

    
    
    """

    def minWindow(self, s: str, t: str) -> str:
        required: Dict[str, int] = {}
        for i in range(0, len(t)):
            c = t[i]
            if c in required:
                required[c] += 1
            else:
                required[c] = 1

        need = len(required.keys())

        print(f"need: {need}, required: {required}")

        left = 0
        right = -1
        min_size = -1
        min_left = -1
        min_right = -1
        formed = 0
        letter_tracker: Dict[str, int] = {}
        for key in required.keys():
            letter_tracker[key] = 0

        while left < len(s):

            if formed < need and right + 1 < len(s):
                print(f"expand: formed: {formed}, left: {left}, right: {right}")
                right += 1
                c = s[right]
                print(f"right letter: {c}")
                if c in letter_tracker.keys():
                    letter_tracker[c] += 1
                    print(f"letter_tracker: {letter_tracker}")
                    if letter_tracker[c] == required[c]:
                        formed += 1
                        if formed == need:
                            window_size = right - left + 1
                            print(f"formed {formed} == need, window_size: {window_size}, min_size: {min_size}")
                            if window_size < min_size or min_size == -1:
                                min_size = window_size
                                min_left = left
                                min_right = right
            else:
                print(f"shrink: formed: {formed} left: {left}, right: {right}")
                c = s[left]
                print(f"left letter: {c}")
                if c in letter_tracker.keys():
                    letter_tracker[c] -= 1
                    print(f"letter_tracker: {letter_tracker}")
                    if letter_tracker[c] < required[c]:
                        formed -= 1
                        print(f"formed: {formed}")
                left += 1
                if formed == need:
                    window_size = right - left + 1
                    print(f"formed {formed} == need, window_size: {window_size}, min_size: {min_size}")
                    if window_size < min_size:
                        min_size = window_size
                        min_left = left
                        min_right = right
        if min_size == -1:
            return ""

        return s[min_left: min_right+1]
    
def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    #s = "aa"
    #t = "aa"

    sol = Solution()
    print(sol.minWindow(s, t))

main()


