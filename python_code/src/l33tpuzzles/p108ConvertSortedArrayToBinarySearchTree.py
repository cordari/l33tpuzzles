# Definition for a binary tree node.
from typing import List, Optional

"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:
                   [0]
                  /   \
              [-3]     [9]
            /         /
       [-10]       [5]      
 
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:


          [0]
         /   \
    [-10]     [5]
        \        \
         [-3]     [9]   



Example 2:

     [3]         [1]
    /               \
 [1]                 [3]

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    the root is the mid element of the array slice. then pass the left portion and right portion recursively to form left subtree and right subtree
    
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode()
        start = 0
        end = len(nums) - 1
        self.bst_helper(nums, start, end, dummy, "left")

        return dummy.left

    def bst_helper(self, nums:List[int], start: int, end: int, parent: TreeNode, dir: str):
        if start > end:
            return
        
        rt_idx = (start + end) // 2
        root_val = nums[rt_idx]
        root = TreeNode(val=root_val)
        if dir == "left":
            parent.left = root
        elif dir == "right":
            parent.right = root

        self.bst_helper(nums, start, rt_idx - 1, root, "left")
        self.bst_helper(nums, rt_idx + 1, end, root, "right")
