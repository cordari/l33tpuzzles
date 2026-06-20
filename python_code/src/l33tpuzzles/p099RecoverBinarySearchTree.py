# Definition for a binary tree node.
from typing import List, Optional

"""
99. Recover Binary Search Tree

Medium

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

 

Example 1:

              [.1.]                   [ 3 ]
             /                       /
        [.3.]           ===>    [ 1 ]
             \                       \
              [ 2 ]                   [ 2 ]
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:

             [.3.]                      [ 2 ]
            /     \                    /     \
       [ 1 ]       [ 4 ]   ===>   [ 1 ]       [ 4 ]
                  /                           /
             [.2.]                       [ 3 ]
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    O(n) space solution:
    
    do an in-order traversal and put the values in a list. go through the list to find where things are out of order.
    when you find the first out of order pair, the one out of place is the one on the left, i.e. if x[i-1] > x[i], then x[i-1] is out of order, 
    and set x[i] as a candidate for the other out of order one, in case x[i-1] and x[i] are swapped

    if you find a second out of order pair, the one out of place is the one on the right, i.e. if x[j-1] > x[j], then x[j] is out of order

    at the end, swap back the first out of place one with the second out of place one.

    tricks to make things easier here:
    1. instead of putting values on the traversal list, put the tree nodes directly onto the travel list, so later you can swap their values in place
    2. instead of recording the values that are out of place, record the indices of the out of place elements  
    """
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        trave: List[TreeNode] = []
        self.in_order_trave(root, trave)

        rev_1_idx = -1
        rev_2_idx = -1

        for i in range(1, len(trave)):
            if trave[i - 1].val > trave[i].val:
                if rev_1_idx == -1:
                    rev_1_idx = i - 1
                rev_2_idx = i
        tmp = trave[rev_1_idx].val
        trave[rev_1_idx].val = trave[rev_2_idx].val
        trave[rev_2_idx].val = tmp


    def in_order_trave(self, node: TreeNode, trave: List[TreeNode]):
        if node.left:
            self.in_order_trave(node.left, trave)
        trave.append(node)
        if node.right:
            self.in_order_trave(node.right, trave)
        
        