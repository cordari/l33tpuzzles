# Definition for a binary tree node.


from collections import deque
from typing import List, Optional, Tuple

"""

102. Binary Tree Level Order Traversal

Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

            [3]
           /   \
        [9]     [20]
               /   \
           [15]     [7] 

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
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
    create a queue, put the root node in with its level (0)
    create a temp list to hold the vals of current level

    keep dequeue until the queue is empty:
     in the logic, check if the dequeued node's level equals current level;
     if levels don't match, that means the nodes for the current level have been exhausted, put the temp list onto the answer, and create a new empty temp list, and increment the current level
     put the element's node's value onto the temp list
     if the node has left child, add to queue with current level + 1
     if the node has right child, add to queue with current level + 1

     when the loop ends, put the template list onto the answer
    
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans: List[List[int]] = []
        queue = deque()
        level = 0
        level_coll:List[int] = []
        queue.append((level, root))

        while len(queue) > 0:
            elem:Tuple[int, TreeNode] = queue.popleft()
            if elem[0] != level:
                ans.append(level_coll)
                level_coll = []
                level = level + 1
            level_coll.append(elem[1].val)
            if elem[1].left:
                queue.append((level + 1, elem[1].left))

            if elem[1].right:
                queue.append((level + 1, elem[1].right))
        
        ans.append(level_coll)
        return ans
    