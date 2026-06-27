# Definition for a binary tree node.
from typing import Deque, List, Optional, Tuple
"""
111. Minimum Depth of Binary Tree

Easy

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:
            [3]
           /   \
        [9]     [20]
               /    \
           [15]      [7]   
              

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
     the Breadth first search BFS is the better approach because the worst case scenario is O(N)

     the Depth first search (DFS) is the naive approach, but you need to track a global min depth. one small pitfall is the min depth needs to be initialized to a large value, at least
     the max number of nodes in the tree.  one mistake is to assume the height of the binary tree won't exceed lg(N), because the tree could be degenerated. but still, BFS is better.
    
    """


    def minDepth(self, root: Optional[TreeNode]) -> int:
        # using BFS
        if not root:
            return 0
        queue: Deque = Deque()

        queue.append((1, root))
        while len(queue) > 0:
            elem:Tuple[int, TreeNode] = queue.popleft()
            node = elem[1]
            lvl = elem[0]
            if not node.left and not node.right:
                return lvl
            if node.left:
                queue.append((lvl+1, node.left))
            if node.right:
                queue.append((lvl+1, node.right))
            


    def minDepth_DFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_d: List[int] = [50000]

        self.md_helper(root, 1, min_d)
        return min_d[0]


    def md_helper(self, node: TreeNode, lvl: int, min_d: List[int]):
        if not node.left and not node.right:
            min_d[0] = min(min_d[0], lvl)
            return
        if node.left:
            self.md_helper(node.left, lvl+1, min_d)
        if node.right:
            self.md_helper(node.right, lvl+1, min_d)