# Definition for a binary tree node.
from typing import Deque, List, Optional, Tuple

"""
107. Binary Tree Level Order Traversal II
Medium

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:

      [3]
     /   \
  [9]     [20]
         /    \
     [15]      [7]

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    do the regular BFS traversal, i.e. top to bottom, left to right. 

    then in the end, reverse the answer list, then return the answer list
    
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level = 0
        queue = Deque()
        queue.append((level, root))

        ans: List[List[int]] = []
        level_coll: List[int] = []

        while len(queue) > 0:
            elem: Tuple[int, TreeNode] = queue.popleft()
            if elem[0] != level:
                ans.append(level_coll)
                level_coll = []
                level += 1
            node = elem[1]
            level_coll.append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        ans.append(level_coll)
        ans.reverse()
        return ans