"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.

"""



from typing import List


class Solution:
    def strStr_naive(self, haystack: str, needle: str) -> int:
        """
        the naive solution is straight-forward, which results in O(m*n), where m is the
        number of characters in the haystack and n number of chars in the needle
        """
        n = len(needle)

        for i in range(0, len(haystack) - n + 1):
            if haystack[i] == needle[0] and haystack[i + n - 1] == needle[n-1]:
                all_match = True
                for x in range(1, n-1):
                    if haystack[i + x] != needle[x]:
                        all_match = False
                        break
                if all_match:
                    return i

        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        """
        an optimized algorithm is called KMP (Knuth-Morris-Pratt). The key is to build a LPS (longest proper prefix that is
        also a suffix) table, which indicates the longest repeated substrings in the pattern matching some leading substrings in the
        pattern itself. The idea is when the pattern has such repetitions, and when you find a partial match of the pattern in the
        haystack, you don't have to start the matching again from the beginning of the needle; instead, because of the repetition,
        you know the last X matching characters in the needle (also in haystack) are exactly the same as the first X characters in
        the needle, so no need to go back and check them again, and instead directly check with the X+1th character in the needle.

        the algorithm is a bit unintuitive. The build of the LPS array is a dynamic programming approach.
        """

        lps: List[int] = [0 for _ in range(0, len(needle))]

        # build LPS array

        left = 0
        right = 1
        while right < len(needle):
            if needle[left] == needle[right]:
                lps[right] = left + 1
                left += 1
                right += 1
            else:
                if left > 0:
                    left = lps[left - 1]
                else:
                    lps[right] = 0
                    right += 1

        # find the match
        h = 0
        n = 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
                if n == len(needle):
                    return h - n # found the first match, return the matching starting index
            else:
                if n == 0:
                    h += 1
                else:
                    n = lps[n - 1]
        return -1

def main():
    hay = "eeef"
    nee = "eef"
    sol = Solution()
    print(sol.strStr(hay, nee))
       
if __name__ == "__main__":
    main()
