from typing import List
"""
67. Add Binary

Easy

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

class Solution:
    """
    add the bits from least significant to most significant, and calculate the carry.

    get the index correct is one tricky part.  

    use the shorter of the two input strings and start at the end. for the longer string, the index should be offset with the length diff between the two strings.
    for the result, it should have 1 more bit than the longer string, and get rid of the bit in end if it is a leading 0.

    don't forget to set carry = 1 or carry = 0 for each iteration. one bug would be not setting carry = 0 so a previous carry = 1 contaminates the calculation.
    
    """
    def addBinary(self, a: str, b: str) -> str:
        large = a
        small = b

        if (len(a) < len(b)):
            large = b
            small = a

        small_len = len(small)
        large_len = len(large)
        len_diff = large_len - small_len
        res: List[int] = [0] * (large_len + 1)

        carry = 0
        res_idx = large_len
        for i in range(small_len - 1, -1, -1):
            bit_l = int(large[i + len_diff])
            bit_s = int(small[i])
            res_bit = bit_l + bit_s + carry

            if res_bit >= 2:
                carry = 1
                res_bit = res_bit - 2
            else:
                carry = 0
            res[res_idx] = res_bit
            res_idx -= 1
        
        for i in range(len_diff - 1, -1, -1):
            bit_l = int(large[i])
            res_bit = bit_l + carry
            if res_bit >= 2:
                carry = 1
                res_bit = res_bit - 2
            else:
                carry = 0
            res[res_idx] = res_bit
            res_idx -= 1
        res[0] = carry

        if res[0] == 0:
            return "".join(str(x) for x in res[1:])
        return "".join(str(x) for x in res)
    
def main():
    sol = Solution()

    print(sol.addBinary("1010", "1011"))

if __name__ == "__main__":
    main()
        