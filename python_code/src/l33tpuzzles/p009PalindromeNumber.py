"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and x < 10:
            return True
        
        if x < 0 or x % 10 == 0:
            return False
        
        num = x
        rev = 0
        """
        instead of holding the digits in string, which takes O(n) space, do the half-way number comparison which takes O(1) space.
        the idea is to chop the original number digit by digit, and therefore build the reverse number digit by digit
        the half-way point is when the reverse number becomes bigger than the chopped original number.
        they could have the same number of digits (when original number has even number of digits), or the reverse could have 1 more
        digit than the chopped original when it had odd number of digits, and in this case, compare rev // 10 with chopped original
        """
        while (rev < num):
            dig = num % 10
            num = num // 10
            rev = rev * 10 + dig

        return rev == num or rev // 10 == num