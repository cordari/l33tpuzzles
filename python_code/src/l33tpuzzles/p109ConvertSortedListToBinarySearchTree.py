# Definition for singly-linked list.
from typing import List, Optional

"""

109. Convert Sorted List to Binary Search Tree

Medium

Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 10^4].
-10^5 <= Node.val <= 10^5
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    traverse the list and convert the list to an array first,
    then recursively build the array into a height-balanced BST by
    1. passing in the array, with low and high indices, with parent node, and direction
    2. calculate the middle index, and create a TreeNode with val being the array element at middle index
    3. attach the node to the parent based on the passed-in direction
    4. recursive call with new high being mid - 1 for left substree
    5. recursive call with new low being mid + 1 for right subtree
    6. terminal condition is when low > high

    7. in main function, create a dummy TreeNode as the parent of the actual root of the tree, to make the code simple and keep all the logic in the recursive function,
    and in the end, just return the dummy.left 
    
    """
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        nums: List[int] = []

        probe: ListNode = head

        while probe:
            nums.append(probe.val)
            probe = probe.next

        dummy: TreeNode = TreeNode()

        low = 0
        high = len(nums) - 1

        self.bst_helper(nums, low, high, dummy, "left")

        return dummy.left

    def bst_helper(self, nums: List[int], low: int, high: int, parent: TreeNode, dir: str):
        if low > high:
            return 
        
        mid = (low + high) // 2
        val = nums[mid]
        node = TreeNode(val=val)
        if dir == "left":
            parent.left = node
        elif dir == "right":
            parent.right = node

        self.bst_helper(nums, low, mid - 1, node, "left")
        self.bst_helper(nums, mid + 1, high, node, "right")