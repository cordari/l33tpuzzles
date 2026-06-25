# Definition for a binary tree node.
from typing import List, Optional
"""
104. Maximum Depth of Binary Tree

Easy

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    DFS traverse using recursion, while passing the max_depth and update it as necessary.

    depth can start with 1 at root node, so the max_depth is the right answer; if start with 0, max_depth will need to be incremented by 1 at the end of the program.
    
    don't forget to check for empty root node and return 0
    
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_dep:List[int] = [1]
        self.md_helper(root, 1, max_dep)

        return max_dep[0]

    def md_helper(self, node: Optional[TreeNode], curr_dep: int, max_dep:List[int]):
        if not node:
            return
        if node.left:
            self.md_helper(node.left, curr_dep + 1, max_dep)
        if node.right:
            self.md_helper(node.right, curr_dep + 1, max_dep)
        if max_dep[0] < curr_dep:
            max_dep[0] = curr_dep
