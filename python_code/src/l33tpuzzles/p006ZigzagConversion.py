"""
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        My own analysis

        1234567890ABCDEFGHIJK   row = 1

        1 3 5 7 9 A C E G I K   row = 2
        2 4 6 8 0 B D F H J


        1   5   9   C   G   K   row = 3
        2 4 6 8 0 B D F H J
        3   7   A   E   I


        1     7     C     I      row = 4
        2   6 8   B D   H J
        3 5   9 A   E G   K
        4     0     F      


        1       9       G      row = 5
        2     8 0     F H
        3   7   A   E   I
        4 6     B D     J
        5       C       K


        if each down + up-and-right is considered a block, the number of characters in the block is X = n + (n-2), where n is the number of rows and (n-2) must be >= 0

        number of blocks is integer div of the block size.

        0th row consists of chars of position 0,        0+X,         0+2X,         0+3X... as long as it doesn't exceed string length
        1st row consists of chars of position 1, 0+X-1, 1+X, 0+2X-1, 1+2X, 0+3X-1, 1+3X... as long as 0+?X-1 > n*(?-1)X
        2nd row consists of chars of position 2, 0+X-2, 2+X, 0+2X-2, 2+2X, 0+3X-2, 2+3X... as long as 0+?X-2 > n*(?-1)X
        ...

        but actually since we know the block size is X = n + (n-2), the (n-2) indicates the number of chars in the diagonal part

        """
        converted = ""
        slen = len(s)
        diag_size = numRows - 2 if numRows - 2 > 0 else 0
        block_size = numRows + diag_size
        print(f"block size: {block_size}")
        block_count = slen // block_size + (1 if slen % block_size > 0 else 0)
        print(f"block_count: {block_count}")

        for i in range(0, numRows):
            for j in range(0, block_count + 1):
                index = i + j * block_size
                if index < slen:
                        
                    converted = converted + s[index]
                    if i != 0 and i != numRows - 1 and diag_size > 0:
                        # first and last rows have no diagnals other rows do have diagnals
                        diag_index = (j + 1) * block_size - i
                        if diag_index < slen:
                            converted = converted + s[diag_index]

        return converted

        """
        another way is to keep a list of strings corresponding to the number of rows
        then go through each character of the string, and append it to the correct string.
        to find the correct index of the string from the list, keep a direction, and flip the direction when the row
        reaches the first row or the last row
        """
    
def main():
    solution = Solution()
    ans = solution.convert("AB", 1)

    print(ans)

    print(12 %1)

if __name__ == "__main__":
    main()
