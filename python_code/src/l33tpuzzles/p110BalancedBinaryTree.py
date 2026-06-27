# Definition for a binary tree node.
from typing import List, Optional, Tuple
"""
110. Balanced Binary Tree

Easy

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:
        [3]
       /   \
    [9]     [20]
           /    \
       [15]      [7]       

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
                          [1]
                         /   \
                      [2]     [2]
                     /   \
                  [3]     [3]
                 /   \
              [4]     [4]            

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    the problem description provides the definition of a balanced binary tree, so the algorithm should code to that.

    for each node, check if its left subtree is balanced. if not, return with not balanced
    if left subtree is balanced, check if its right subtree is balanced. if not, return with not balanced.

    if both subtrees are balanced, use the returned subtree heights to compare the left and right subtree height.

    left subtree height is the max of the two heights returned from the left subtree balance check 
    right subtree height is the max of the two heights return from the right subtree balance check

    if left height and right height diff more than 1, return not balanced, else return balanced, and for left and right height, each should be incremented by 1 to account for the current node


    the WRONG way to approach this is to try to find the shortest height and the longest height of the entire tree and see if they differ more than 1, because this would incorrectly determine
    the following balanced tree to be not balanced:

            1
           /  \
          2    3
         / \   /
        4  5   6
       /
      8 
    
    """


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        result = self.bal_helper(root)

        return result[2]
    
    def bal_helper(self, node:Optional[TreeNode]) -> Tuple[int, int, bool]:
        if not node:
            return (0, 0, True)
        
        left_result = self.bal_helper(node.left)
        if not left_result[2]:
            return left_result
        
        right_result = self.bal_helper(node.right)
        if not right_result[2]:
            return right_result
        
        left_h = max(left_result[0], left_result[1])
        right_h = max(right_result[0], right_result[1])

        
        return (left_h + 1, right_h + 1, abs(right_h-left_h) <= 1)


        