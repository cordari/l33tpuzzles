package main.java.cordari.lt2026._007reverseinteger;

/**
 * 7. Reverse Integer


Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

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
 */
public class Solution {

    /*
     * because Java int only holds 32-bit, and the problem prohits use of long, so we must do overflow
       check before the number overflows.  The checks should be done before doing current reversed value * 10
       1. if current reversed value > MAX / 10, then * 10 would cause overflow
       2. if current reversed value == MAX / 10, then need to check if the new digit being appened would cause it to overflow

       Using Java is actually easier than Python. Even though Python allow arbitrary number of digits for integer, it
       is still needed to implement the boundary check so we don't cheat using language-specific feature.  

       But on top of that, python's mod (%) and integer division (//) with negative numbers behave differently
       from these in Java. Python uses floor, instead of Java's rounding down, so for python, dealing with negative
       number could be tricky if one is not that familiar with these nuances.
     */
    public int reverse(int x) {
        final int HIGH_BOUND = Integer.MAX_VALUE / 10;
        final int LOW_BOUND = Integer.MIN_VALUE / 10;
        final int HIGH_BOUND_DIGIT = Integer.MAX_VALUE - HIGH_BOUND * 10;
        final int LOW_BOUND_DIGIT = Integer.MIN_VALUE - LOW_BOUND * 10;

        System.out.println("LOW_BOUND_DIGIT: " + LOW_BOUND_DIGIT);

        int reversed = 0;

        if (x >= -9 && x <= 9) {
            return x;
        }
        int rest = x;

        if (x < 10) {
            while (rest != 0) {
                final int lastDigit = rest % 10;
                System.out.println("lastDigit: " + lastDigit);
                rest = rest / 10;
                if (reversed < LOW_BOUND)
                    return 0;
                else if (reversed == LOW_BOUND && lastDigit < LOW_BOUND_DIGIT)
                    return 0;
                else {
                    reversed = reversed * 10 + lastDigit;
                }
            }
        } else {
            while (rest != 0) {
                final int lastDigit = rest % 10;
                rest = rest / 10;
                if (reversed > HIGH_BOUND)
                    return 0;
                else if (reversed == HIGH_BOUND && lastDigit > HIGH_BOUND_DIGIT)
                    return 0;
                else {
                    reversed = reversed * 10 + lastDigit;
                }
            }
            
        }


        return reversed;
    }

    public static void main() {
        Solution sol = new Solution();
        System.out.println(sol.reverse(-2147483412));
    }
}
