"""
69. Sqrt(x)

Easy

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1

"""

class Solution:
    """
    pretty straight forward. using binary search to find the largest
    integer whose square is <= x.  Keep a variable to track
    the highest integer seen so far that's <= x

    start with [0, x].

    make sure
    1. while condition is low <= high
    2. when search left, high = mid - 1
    3. when search right, low = mid + 1
    
    """
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        low = 1
        high = x
        highest = 1

        while low <= high:
            mid = (low + high) // 2
            prod = mid * mid
            if prod > x:
                high = mid - 1
            else:
                highest = max(highest, mid)
                low = mid + 1

        return highest
    
def main():
    sol = Solution()
    print(sol.mySqrt(625))

if __name__ == "__main__":
    main()
