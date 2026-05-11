"""

29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is strictly greater than 2^31 - 1,
  then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""

class Solution:
    """
    doing integer division without using divide or multiplication - the algorithm is as follows:
    1. doubling the divisor (by either adding divisor to itself, or shifting left) until the divisor cannot be doubled or else it would exceed the dividend
    2. count the number of times it was doubled, and 2^n is added to the quotient. substract the latest doubled divisor from dividend to get the remaining dividend value
    3. repeat until the remaining dividend value is less than the divisor

    since the problem has an overflow check constraint and limits the number size to be 32-bit, below are some of the caveats:
    1. use negative values for divisor, dividend, doubling of the divisor, quotient etc.  because negative value can hold 1 more value than the positive value due to 0.  negative -2^31, positive 2^31 - 1
    2. because of the use of negative values, comparisons are flipped. think in terms of abs value. if abs(remain) < abs(divisor), we should write if remain > divisor 
    3. need to check for boundary condition before doubling the divisor. if doubling the current divisor is going to exceed the boundary, it means the current divisor is already exceeding half of the boundary. since the
       boudary is - 2^31, half of it is -2^30    
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        # POS_CRITICAL = 2**30
        NEG_CRITICAL = -1 * 2**30
        NEG_BOUND = -1 * 2**31

        sign = 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        # using negative numbers as they can accomodate a bigger value (- 2^31) than positive number (2^31 - 1)
        remain = -1 * dividend if dividend > 0 else dividend
        
        dvsr = -1 * divisor if divisor > 0 else divisor

        if dvsr < remain:
            print("return 0")
            return 0
        
        quotient = 0
        

        while remain <= dvsr:
            doubling = dvsr
            shift_count = 0
            # because we are using negative numbers, we use >= here
            while doubling >= NEG_CRITICAL and (doubling << 1) >= remain:
                doubling = doubling << 1
                shift_count += 1
            quotient -= 2 ** shift_count
            remain -= doubling
        
        
        # handle the only possible overflow case, which is when sign is positive, and value is 2^31
        # because negative 2^31 is allowed, but positive only allows up to 2^31-1.
        if sign == 1 and quotient == NEG_BOUND:
            return 2**31 - 1 # positive boundary
        
        if sign == 1:
            return 0 - quotient
    
        return quotient
    
def main():
    sol = Solution()
    x = sol.divide(-10, 10)
    print(x)

if __name__ == "__main__":
    main()

