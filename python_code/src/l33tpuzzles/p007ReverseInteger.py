"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        python allows arbitrary number of bits in integer, so this problem is really designed for more constrained languages such as java.

        but we can still perform the boundary checks.  the boundary checks consist of:
         1. before taking the current reversed value * 10, check if the current reversed value is > MAX // 10 (similar for negative number)
         2. if current reversed value == MAX // 10, check if the new digit to be appended would bring the new reversed number > MAX (similar for neg number)

        however, python does have its own got-yous, which is the behavior of mod % and integer division // with negative number uses
        floor (round towards negative infinity).
        """

        INT32_MAX = 2**31 - 1
        INT32_MIN = -1 * 2**31

        high_bound = INT32_MAX // 10
        low_bound = int(INT32_MIN / 10)

        high_bound_digit = INT32_MAX - high_bound * 10
        low_bound_digit = INT32_MIN - low_bound * 10

        if x >= -9 and x <= 9:
            return x
        
        is_negative = x < 0

        rest = x

        reversed = 0

        if is_negative:
            while rest != 0:
                # python negative mod used floor, so must use negative divisor to get the proper digit
                last_dig = rest % -10
                
                # python integer division also uses floor, so -1 // 10 always returns -1, and won't become 0
                # so must use float division and then convert to int
                rest = int(rest / 10)
                
                if reversed < low_bound:
                    return 0
                elif reversed == low_bound and last_dig < low_bound_digit:
                    return 0
                else:
                    # still use + last_dig here because last_dig itself is negative
                    reversed = reversed * 10 + last_dig
                
        else:
            while rest != 0:
                last_dig = rest % 10
                
                rest = rest // 10
                
                if reversed > high_bound:
                    return 0
                elif reversed == high_bound and last_dig > high_bound_digit:
                    return 0
                else:
                    reversed = reversed * 10 + last_dig

        return reversed
    
def main():
    sol = Solution()
    print(sol.reverse(-120))
    
if __name__ == "__main__":
    main()

            