"""
50. Pow(x, n)

Medium

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= x^n <= 10^4
"""

class Solution:

    """
    the idea is to keep squaring the base, i.e. doubling the power from 1 until it exceeds the original power. Then accumulate the base doubling value, deduct the last power from the original power and start the process again until the remaining power is 0.

    if the original power is negative, keep a flag and use absolute value of the power. if the power is negative, return the reciprocal of the accumulated value; otherwise return the accumulated value
    
    """
    
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        
        neg_power = n < 0
        abs_pow = abs(n)

        curr_pow = 1  # start power with 1
        remain_pow = abs_pow # initial remaining power is the original power (absolute value of it)

        ans = 1  # final answer
        accumulate = x # keeps the doubling of the base
        
        while remain_pow > 0:
            if curr_pow * 2 <= remain_pow: # if doubling won't exceed the remaining power, doubling it
                accumulate *= accumulate
                curr_pow *= 2
            else:                          # otherwise, take what's doubled so far and accumulate to the final answer. deduct the power to get the new remaining power and start again
                remain_pow = remain_pow - curr_pow
                curr_pow = 1
                ans *= accumulate
                accumulate = x

        if neg_power:           # return reciprocal if power was negative
            return 1 / ans
        else:
            return ans
        
def main():
    sol = Solution()

    print(sol.myPow(-2.0, 3))

if __name__ == "__main__":
    main()