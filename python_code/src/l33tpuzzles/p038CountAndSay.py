"""
38. Count and Say

Medium

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the run-length encoding of countAndSay(n - 1).
Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

Given a positive integer n, return the nth element of the count-and-say sequence.

 

Example 1:

Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
Example 2:

Input: n = 1

Output: "1"

Explanation:

This is the base case.

 

Constraints:

1 <= n <= 30
 

Follow up: Could you solve it iteratively?
"""

from typing import List, Tuple


class Solution:
    """
    straight-forward iteration, using the base case, and then loop through subsequent iterations to generate the output, and then set the input to the output for the subsequent iteration

    keep a list of tuples. list preserves the order, and the tuple holds the count of the value.

    the first char in the input string is the initial val, and the count starts with 1
    go through the rest of the string char by char
      if char matches current val, increment the count
      else
        add tuple (count, val) to the list
        val is now the current char, and count resets to 1
    after the loop, add another tuple (count, val) to the list
    then go through the list of tuples to generate the string
    assign the new string to the input for next iteration
    
    """
    def countAndSay(self, n: int) -> str:
        compress = "1"

        for i in range(1, n):
            count_val: List[Tuple[int, str]] = []
            count = 1
            val = compress[0]
            for p in range(1, len(compress)):
                if compress[p] == val:
                    count += 1
                else:
                    count_val.append((count, val))
                    count = 1
                    val = compress[p]
            count_val.append((count, val))
            output = ""
            for t in count_val:
                output = output + str(t[0]) + t[1]
            compress = output

        return compress
    
def main():
    sol = Solution()
    print(sol.countAndSay(4))

if __name__ == "__main__":
    main()


        