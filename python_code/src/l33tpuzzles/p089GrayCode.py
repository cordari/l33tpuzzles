from typing import List
"""
89. Gray Code

Medium

An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

 

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]
 

Constraints:

1 <= n <= 16

"""

class Solution:
    """
    there are multiple different gray code sequences, but for this problem, it could use the mirror and append method, which is one of ways to generate gray code

    n = 1:  [0, 1]
    n = 2:
      1. mirror the n = 1 answer backwards and append to the answer: [0, 1, 1, 0]
      2. for the latter half of the answer, pre-pend a leading 1 bit:  [00, 01, 11, 10]
    n = 3:
      1. mirror the n = 2 answer backwards and append to the answer: [00, 01, 11, 10, 10, 11, 01, 00]
      2. pre-pend a leading 1 bit to the latter half of the answer:  [000, 001, 011, 010, 110, 111, 101, 100]
    
    and so on...

    """
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        ans = [0, 1]
        if n == 1:
            return ans
        
        for i in range(1, n):
            l = len(ans)
            # mirror
            for j in range(l - 1, -1, -1):
                ans.append(ans[j])
            one = 1 << i  # the leading 1 is 1 left shift to n-1 bits
            for j in range(l, l*2):
                ans[j] = one + ans[j]
        
        return ans
    
def main():
    sol = Solution()
    print(sol.grayCode(3))

main()