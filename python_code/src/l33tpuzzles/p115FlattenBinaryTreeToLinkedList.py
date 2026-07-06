# Definition for a binary tree node.
from typing import List, Optional
"""

114. Flatten Binary Tree to Linked List

Medium

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:
         [1]           [1]
        /   \             \
     [2]     [5]           [2]
    /   \       \             \
 [3]     [4]     [6]           [3]
                                  \
                                   [4]
                                      \
                                       [5]
                                          \
                                           [6]      


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        
        if not root.left and not root.right:
            return root
        
        prev: List[Optional[TreeNode]] = [None]
        head = self.fl_helper(root, prev)

        return head
        
    
    def fl_helper(self, node:TreeNode, prev: List[Optional[TreeNode]]) -> TreeNode:
        head: Optional[TreeNode] = None
        if node.right:
            head = self.fl_helper(node.right, prev)
            prev[0] = head
        if node.left:
            head = self.fl_helper(node.left, prev)
            prev[0] = head
        node.right = prev[0]
        node.left = None
        prev[0] = node
        return node
        
        