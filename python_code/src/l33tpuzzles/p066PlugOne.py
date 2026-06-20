from typing import List
"""

66. Plus One

Easy

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

class Solution:
    """
    since it is only plus one, the result will have the same number of digits as input, or with 1 more digit. allocate 1 more for result, and get rid of it in the end if the leading number is 0

    for the first digit, add 1; for other digits add carry.
    
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        result: List[int] = [0] * (len(digits) + 1)

        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            dig = digits[i]
            if i == len(digits) - 1:
                dig = dig + 1
            else:
                dig = dig + carry
            if dig > 9:
                dig = dig - 10
                carry = 1
            else:
                carry = 0
            result[i + 1] = dig
        result[0] = carry

        if result[0] == 0:
            return result[1:]
        return result
    
def main():
    sol = Solution()

    print(sol.plusOne([9,9,9]))

if __name__ == "__main__":
    main()