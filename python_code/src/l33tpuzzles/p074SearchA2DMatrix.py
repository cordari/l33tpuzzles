from typing import List
"""
74. Search a 2D Matrix

Topics

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

"""

class Solution:
    """
    first use binary search to locate the potential row that may contain the target, then use binary search in the row to check if it contains the target.

    to find the row, initialize the potential row to be -1. during binary search, set potential row to mid when matrix[mid][0] < target

    for binary search, condition is always while low <= high, and when shifting, low = mid + 1, and high = mid - 1, always
    
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        

        low = 0
        high = row - 1

        target_row = low if low == high else -1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] < target:
                target_row = mid
                low = mid + 1
            elif matrix[mid][0] == target:
                return True
            else:
                high = mid - 1

        if target_row == -1:
            return False
        
        low = 0
        high = col - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[target_row][mid] < target:
                low = mid + 1
            elif matrix[target_row][mid] == target:
                return True
            else:
                high = mid - 1

        return False
    
def main():
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 9
    mat = [[1]]
    target = 0
    sol = Solution()
    print(sol.searchMatrix(mat, target))

main()