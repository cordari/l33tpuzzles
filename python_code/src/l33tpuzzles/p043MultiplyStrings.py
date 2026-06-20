"""
43. Multiply Strings

Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.

"""

class Solution:
    """
    the algorithm is pretty much how we do multiplication by hand.

    the shorter number as the outer loop, so each digit multiplies each digit of the longer number.
    go from the last character to the first character, i.e. from least signficant digit to the most significant digit
    keep the digits as numbers for each "row"
    keep a list of rows, and at the end, sum up these rows to get the final product
    keep the digits of the final product in a list
    and as a final step, go backwards on the product list to generate the string. make sure to skip the leading 0s

    some differences are:
    
    1. instead of shifting positions, insert trailing 0s for each "row" to make the summing easier
    2. it also makes things a lot easier to insert leading 0s for each "row".  When a M-digit number multiplies with a N-digit number, the result will have at most M+N digits.
    3. having leading and trailing 0's makes all rows have the same number of digits, making the sum easier 
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1

        big = num1
        small = num2

        if len(num2) > len(num1):
            big = num2
            small = num1

        rows = []
        for i in range(len(small) - 1, -1, -1):
            carry = 0
            small_dig = small[i]
            row_prod = []
            for k in range(len(small) - 1, i, -1): # fill in trailing 0s
                row_prod.append(0)
            for j in range(len(big) - 1, -1, -1):
                big_dig = big[j]

                prod = int(small_dig) * int(big_dig) + (carry)

                prod_dig = prod % 10
                carry = prod // 10
                row_prod.append(prod_dig)
            row_prod.append(carry)
            for k in range(len(row_prod), len(small) + len(big)): # fill in leading 0s
                row_prod.append(0)
            print(row_prod)
            rows.append(row_prod)

        size = len(rows[-1])

        carry = 0
        digs = "0123456789"
        prod = []
        for i in range(0, size):
            sum = 0
            for j in range(0, len(rows)):
                sum += rows[j][i]
            sum += carry
            dig = sum % 10
            carry = sum // 10
            prod.append(dig)
        prod.append(carry)

        # by now, prod has all the digits, in reverse order, with possible leading zeros

        ans =  ""
        seen_leading_non_zero = False
        for i in range(len(prod) - 1, -1, -1):  # convert the prod digits to strings digit by digit, in reverse order, and also ignore leading zeros
            dig = prod[i]
            if dig != 0 or seen_leading_non_zero:
                seen_leading_non_zero = True
                ans = ans + digs[dig]

        return ans
    
def main():
    sol = Solution()
    print(sol.multiply("123", "456"))

if __name__ == "__main__":
    main()
                

        
        


