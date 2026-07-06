# Definition for a binary tree node.
from typing import Optional

"""
112. Path Sum
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    straight-forward recursive algorithm.

    pass in the current node and the remaining target sum.

    compute the remaining target sum by substracting node.val from the passed-in target sum.

    if the remaining target is 0, and the node has no left nor right, return True

    otherwise if node has left child, recursive call with left child and the remaining sum. if the call comes back True, return True

    otherwise if node has right child, recursive call with right child and the remaining sum. if the call comes back True, return True

    else return False
    
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        has_path = self.ps_helper(root, targetSum)
        return has_path
    
    def ps_helper(self, node: TreeNode, target: int) -> bool:
        val = node.val
        new_target = target - val

        if not node.left and not node.right and new_target == 0:
            return True

        if node.left:
            has_path = self.ps_helper(node.left, new_target)
            if has_path:
                return True
        if  node.right:
            has_path = self.ps_helper(node.right, new_target)
            if has_path:
                return True
        return False
        