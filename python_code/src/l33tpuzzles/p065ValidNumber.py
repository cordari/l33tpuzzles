"""

65. Valid Number

Hard

Given a string s, return whether s is a valid number.

For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

Formally, a valid number is defined using one of the following definitions:

An integer number followed by an optional exponent.
A decimal number followed by an optional exponent.
An integer number is defined with an optional sign '-' or '+' followed by digits.

A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:

Digits followed by a dot '.'.
Digits followed by a dot '.' followed by digits.
A dot '.' followed by digits.
An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

The digits are defined as one or more digits.

 

Example 1:

Input: s = "0"

Output: true

Example 2:

Input: s = "e"

Output: false

Example 3:

Input: s = "."

Output: false

 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""

from typing import List


class Solution:
    """
    implement a state machine. Don't use state + event -> state table, and it would be too formal and too much work. Just use logic to impelement the state.  The tricky
    one would be around ".".  a number + "." is valid; "." + number also valid, but "." alone is not.
    
    """
    def isNumber(self, s: str) -> bool:
        # STATES:
        BEGIN = 0
        GOT_SIGN = 1
        GOT_INT = 2
        GOT_DECI_POINT_WITH_LEAD = 3
        GOT_DECI_POINT_WITHOUT_LEAD = 10
        GOT_DECIMAL = 4
        GOT_E = 5
        GOT_E_SIGN = 6
        GOT_E_INT = 7
        
        state = BEGIN

        for i in range(0, len(s)):
            char = s[i]
            if char == "-" or char == "+":
                if state == BEGIN:
                    state = GOT_SIGN
                elif state == GOT_E:
                    state = GOT_E_SIGN
                else:
                    return False
            elif char >= "0" and char <= "9":
                if state == BEGIN or state == GOT_SIGN or state == GOT_INT:
                    state = GOT_INT
                elif state == GOT_DECI_POINT_WITH_LEAD or state == GOT_DECI_POINT_WITHOUT_LEAD or state == GOT_DECIMAL:
                    state = GOT_DECIMAL
                elif state == GOT_E or state == GOT_E_SIGN or state == GOT_E_INT:
                    state = GOT_E_INT
                else:
                    return False
            elif char == ".":
                if state == BEGIN or state == GOT_SIGN:
                    state = GOT_DECI_POINT_WITHOUT_LEAD
                elif state == GOT_INT:
                    state = GOT_DECI_POINT_WITH_LEAD
                else:
                    return False
            elif char == "e" or char == "E":
                if state == GOT_INT or state == GOT_DECI_POINT_WITH_LEAD or state == GOT_DECIMAL:
                    state = GOT_E
                else:
                    return False
            else:
                return False
            print(f"char is {char}, state={state}")
        if state == BEGIN or state == GOT_SIGN or state == GOT_DECI_POINT_WITHOUT_LEAD or state == GOT_E or state == GOT_E_SIGN:
            return False
        return True
    
def main():
    sol = Solution()
    print(sol.isNumber("92e1740e91"))

if __name__ == "__main__":
    main()