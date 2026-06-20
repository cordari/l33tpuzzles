"""

87. Scramble String

Hard

We can scramble a string s to get a string t using the following algorithm:

If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.

 

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Explanation: One possible scenario applied on s1 is:
"great" --> "gr/eat" // divide at random index.
"gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
"gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
"g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
"r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
"r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
The algorithm stops now, and the result string is "rgeat" which is s2.
As one possible scenario led s1 to be scrambled to s2, we return true.
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
Example 3:

Input: s1 = "a", s2 = "a"
Output: true
 

Constraints:

s1.length == s2.length
1 <= s1.length <= 30
s1 and s2 consist of lowercase English letters.

"""

from typing import Dict, Tuple


class Solution:
    """
    solution is recursion with memoization.

    for the strings, split at every possible location, and use recursion to check if the substrings are scrambles. there are two scenarios:
    1. cut at the same location:
       s1  [ x-chars ][   y-chars   ]
       s2  [ x-chars ][   y-chars   ]
       use recursion to check check if s1 first portion is scramble of s2 first portion, AND if s1 second portion is scramble of s2 second portion
    2. cut at reverse location:
       s1  [ x-chars ][   y-chars   ]
       s2  [   y-chars   ][ x-chars ]
       this is the swapped scenario
       use recursion to check if s1 first portion is scramble of s2 second portion, AND if s1 second portion is scramble of s2 first portion

    if using naive recursion, it would run out of time. so add two optimizations
    
    1. use letter frequency count on strins to prune. for substrings to be scrambles, their letter frequency count have to be the same
    2. use memoization to memorize answers that have already been computed


    in this implementation, figuring out the index is a bit tricky.  

    the recursive function passes in the entire s1 and s2, but using s1i and s2i as the starting indices to mark the substring starting indices
    within s1 and s2, and length to mark the length of the substring.
    
    """

    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.is_scram(s1, s2, 0, 0, len(s1), memo)
    

    def is_scram(self, s1: str, s2: str, s1i: int, s2i: int, length: int, memo: Dict[Tuple[int, int, int], bool]) -> bool:
        # check memoization
        if (s1i, s2i, length) in memo:
            return memo[(s1i, s2i, length)]
        
        # base case of 1 character
        if length == 1:
            return s1[s1i] == s2[s2i]
        
        # pruning by checking letter frequency
        s1_freq: Dict[str, int] = {}
        s2_freq: Dict[str, int] = {}

        for i in range(s1i, s1i + length):
            c = s1[i]
            if c in s1_freq:
                s1_freq[c] += s1_freq[c]
            else:
                s1_freq[c] = 1

        for i in range(s2i, s2i + length):
            c = s2[i]
            if c in s2_freq:
                s2_freq[c] += s2_freq[c]
            else:
                s2_freq[c] = 1

        # if letter frequency don't match, they are not scramble of each other
        if s1_freq != s2_freq:
            memo[(s1i, s2i, length)] = False
            return False
        
        # try all split points
        for i in range(1, length):
            # cut both s1 and s2 at the same location, and check if their first portions match and their second portions match
            if self.is_scram(s1, s2, s1i, s2i, i, memo) and self.is_scram(s1, s2, s1i + i, s2i + i, length - i, memo):
                memo[s1i, s2i, length] = True
                return True
            # cut s1 and s2 at reversed location, and check if first portion of s1 matches second portion of s2, and second portion of s1 matches first portion of s1
            if self.is_scram(s1, s2, s1i, s2i + length - i, i, memo) and self.is_scram(s1, s2, s1i + i, s2i, length - i, memo):
                memo[s1i, s2i, length] = True
                return True
            
        memo[s1i, s2i, length] = False
        return False

def main():
    s1 = "great"
    s2 = "rgeat"
    s1 = "abcde"
    s2 = "caebd"
    sol = Solution()
    print(sol.isScramble(s1, s2))

main()
