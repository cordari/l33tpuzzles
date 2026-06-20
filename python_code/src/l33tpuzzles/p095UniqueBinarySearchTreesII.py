# Definition for a binary tree node.
from typing import Dict, List, Optional, Tuple
"""
95. Unique Binary Search Trees II

Medium

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:

[1]       [1]              [2]               [3]       [3]
   \         \            /   \             /          /
    [3]       [2]      [1]     [3]       [2]        [1]
   /             \                      /              \
[2]               [3]                [1]                [2]
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    recursion with memoization

    the root node can be any number in the current list.  with BST, numbers less than the root node number will always be in the left subtree, and numbers greater than the root node number will
    always be in the right subtree.

    when the recursive call to form the left subtrees returns, and the recursive call to form the right subtrees returns, the different tree structure would be the cartesian products between the
    left subtrees and right subtrees.

    use start and end to bound the sublist, and the start and end also form the memoization key
    
    """
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        start = 1
        end = n
        mem: Dict[Tuple[int, int], List[Optional[TreeNode]]] = {}
        res = self.gen_helper(start, end, mem)

        return res

    def gen_helper(self, start: int, end: int, mem: Dict[Tuple[int, int], List[Optional[TreeNode]]]) -> List[Optional[TreeNode]]:
        if (start, end) in mem:
            return mem[(start, end)]
        if start > end:
            return []
        if start == end:
            return [TreeNode(val=start)]
        
        result = []
        for i in range(start, end + 1):
            node = TreeNode(val=i)
            left = self.gen_helper(start, i - 1, mem)
            right = self.gen_helper(i + 1, end, mem)
            if len(left) == 0 and len(right) == 0:
                result.append(TreeNode(val=i))
            elif len(left) == 0:
                for rnode  in right:
                    node = TreeNode(val=i, right=rnode)
                    result.append(node)
            elif len(right) == 0:
                for lnode in left:
                    node = TreeNode(val=i, left=lnode)
                    result.append(node)
            else:
                for lnode in left:
                    for rnode in right:
                        node = TreeNode(val=i, left=lnode, right=rnode)
                        result.append(node)
        mem[(start, end)] = result
        return result