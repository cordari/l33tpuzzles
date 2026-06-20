# Definition for a binary tree node.
from typing import Optional
"""

101. Symmetric Tree

Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:
                  [1]
               /   :   \
            [2]    :    [2]
           /   \   :   /   \
        [3]    [4] : [4]     [3]
                   :
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
              [1]
             /   \
          [2]     [2]
             \        \
              [3]      [3]   

Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_symm(root.left, root.right)

    def is_symm(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if (left and not right) or (right and not left):
            return False
        
        if not left and not right:
            return True
        
        if left.val != right.val:
            return False
        
        if not self.is_symm(left.left, right.right):
            return False
        
        if not self.is_symm(left.right, right.left):
            return False
        
        return True