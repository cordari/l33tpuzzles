# Definition for a binary tree node.
from typing import Optional
"""
100. Same Tree

Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_same(p, q)

    def is_same(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if (n1 and not n2) or (n2 and not n1):
            return False
        
        if not n1 and not n2:
            return True

        if n1.val != n2.val:
            return False

        if not self.is_same(n1.left, n2.left):
            return False

        if not self.is_same(n1.right, n2.right):
            return False
        
        return True
