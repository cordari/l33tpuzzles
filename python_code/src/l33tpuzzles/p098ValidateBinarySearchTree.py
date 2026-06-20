# Definition for a binary tree node.
from typing import Optional
"""
98. Validate Binary Search Tree

Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    the key to solution is passing the correct boundary down the subtree.

    at root node, there is no boundary as the root node can have any value

    when going down the left subtree, the parent's value becomes the new max / right boundary
    when going down the right subtree, the parent's value becomes the new min / left boundary

    caveat: since boundary can be optional, check explicitly for if min != None or if max != None, instead of just if min or if max, because the latter would fail when min or max is 0 
    
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root.left:
            result = self.is_valid(root.left, None, root.val)
            if not result:
                return False
        if root.right:
            result = self.is_valid(root.right, root.val, None)
            if not result:
                return False
        return True

    def is_valid(self, node: TreeNode, min: Optional[int], max: Optional[int]) -> bool:
        val = node.val

        if max != None and val >= max:
            return False
        
        if min != None and val <= min:
            return False

        
        if node.left:
            result = self.is_valid(node.left, min, node.val)
            if not result:
                return False
        if node.right:
            result = self.is_valid(node.right, node.val, max)
            if not result:
                return False
        return True
