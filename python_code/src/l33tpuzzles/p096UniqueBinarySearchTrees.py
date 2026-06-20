"""
96. Unique Binary Search Trees

Medium

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 19

"""
from typing import List


class Solution:
    """
    DP problem. the number of tree structures has to do with number of nodes, and has nothing to do with the values in the nodes.

    DP[x] = number of tree structures for x nodes
    set base cases:
    DP[0] = 1, meaning there is 1 tree structure for an empty sub tree
    DP[1] = 1, there is 1 tree structure for a single node

    for DP[2], iterate through 1, then 2.
       when x = 1, there is 0 nodes to the left, 1 node to the right, total = DP[0] x DP[1] = 1x1 = 1
       when x = 2, there is 1 node to the left, 0 nodes to the right, total = DP[1] x DP[0] = 1x1 = 1
       sum = 1+1 = 2

    DP[3], 1 through 3
       x = 1, 0 to left, 2 to right,  total = DP[0] x DP[2] = 1 x 2 = 2
       x = 2, 1 to left, 1 to right, total  = DP[1] x DP[1] = 1 x 1 = 1
       x = 3, 2 to left, 0 to right, total = DP[2] x DP[0] = 2 x 1 = 2
       sum = 5

    ...
    so forth

    
    """
    def numTrees(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)

        dp[0] = 1 # empty subtree
        dp[1] = 1 # single node

        for i in range(2, n+1):
            sum = 0
            for j in range(1, i+1):
                left = j - 1
                right = i - j
                sum += dp[left] * dp[right]
            dp[i] = sum
        return dp[n]
def main():
    sol = Solution()
    print(sol.numTrees(4))

main()