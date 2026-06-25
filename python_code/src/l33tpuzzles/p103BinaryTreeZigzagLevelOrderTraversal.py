# Definition for a binary tree node.
from typing import Deque, List, Optional, Tuple
"""
103. Binary Tree Zigzag Level Order Traversal

Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:
    [3]
   /   \
[9]     [20]
       /    \
    [15]     [7] 


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    although this is very similar to the level order traversal, there are some tricky parts.

    the similar part is:
    1. use a queue and a temp list to collect for the current level
    2. queue up each node with its level
    3. dequeue, and when level from element differs from current level, put the temp list on answer, and start a new empty temp list. But before putting the temp list on answer, need to check the level
      of the list; if level is odd (0-based), reverse the list, before adding onto the answer
    4. if node has left child, enqueue left
    5. if node has right child, enqueue right
    
    6. after loop, check level again; if odd, reverse list.  add the list onto answer

    CAVEAT:
      if doing the level check and try to change the order of the children to be enqueue, that is the WRONG approach, because if at a level, the nodes are queued in the reverse order, their children
      will not be in the correct order as you won't see the children of the left-most node before seeing the children of the right-most node.

      so when enqueuing, you always go from left most to right most, and only when you append the answer, use the level to see if the answer should be reversed or not.

      also don't forget to check the level and do reverse as necessary after the loop
    
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans: List[List[int]] = []

        queue = Deque()

        level = 0

        level_coll: List[int] = []

        queue.append((level, root))

        while len(queue) > 0:
            elem: Tuple[int, TreeNode] = queue.popleft()
            if elem[0] != level:
                if level %2 == 1:
                    level_coll.reverse()
                ans.append(level_coll)
                level_coll = []
                level += 1

            node:TreeNode = elem[1]
            level_coll.append(node.val)

            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))

        if level %2 == 1:
            level_coll.reverse()
        ans.append(level_coll)

        return ans
