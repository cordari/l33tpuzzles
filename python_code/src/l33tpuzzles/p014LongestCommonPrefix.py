"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        straigh-forward implementation, i.e. go through every char, and check if all strings have the same char
        common_prefix = ""
        i = 0
        done = False
        while not done:
            if i >= len(strs[0]):
                break
            curr = strs[0][i]
            j = 1
            while j < len(strs) and not done:
                if i >= len(strs[j]):
                    done = True
                    break
                if strs[j][i] != curr:
                    done = True
                    break
                j += 1
            if not done:
                common_prefix += curr
            i += 1
        return common_prefix
        """


        """"
        a clever solution:
        1. sort the string array
        2. longest common prefix is the common prefix between the first and last elements of the array
        
        """
        if len(strs) == 1:
            return strs[0]
        
        strs.sort()

        first = strs[0]
        last = strs[len(strs) - 1]

        l = min(len(first), len(last))

        common_prefix = ""
        for i in range(0, l):
            if first[i] == last[i]:
                common_prefix += first[i]
            else:
                break
        return common_prefix
    
    
        