# Definition for a binary tree node.
"""
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:
          [3]
         /   \
      [9]     [20]
             /    \
         [15]      [7]

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Dict, List, Optional


class Solution:
    """
    Observations:
    1. the root of a subtree is the first node/value of the pre-order list slice.
    2. for that same root in the in-order list/slice, everything left of the root within the slice is the left subtree of that root; and everything right of the root within the slice is the
      right subtree of that root
    3. in the pre-order list slice, if the tree has left subtree, then the node/value right after the root is the root of the left subtree.
    4. in the pre-order list slice, if the tree has right subtree, then the index of the right subtree root is the root index + left subtree root index + 1
    5. to determine if a root has left or right subtree, use the left slice and right slice size from the in-order list slice


    algorithm:
    1. the first value in the pre-order slice is the root
    2. use that value to find the root's index in the in-order list slice.
    3. if the root's index is between the start and end, then it is valid, create a subtree root node with the root value, and attach it to the passed-in parent node per the direction (left or right)
        passed-in
    4. everything to the left of the root's in-order index in the slice are the left subtree, and everything to the right are the right subtree
    5. if the left subtree size is > 0, it has left subtree, recursively call the helper funtion and update the start and end index of the left in-order slice. the index of the pre-order
       slice is just 1 more than the pre-order index being passed in to the current level
    6. if the right subtree size is > 0, it has right subtree, recursively call the helper function and update the start and end index of the right in-order slice. the index of the pre-order
       slice is the current level pre-order index, plus left subtree size, plus 1.

    7. terminal conditino: if the in-order slice start index > end index, return with no-op. if the pre-order index >= len(pre-order list), return with no op.

    8. tip: create a dummy node at the main function as the ghost root, and make the real root a left child of this ghost root, and in the end, return dummy.left. this makes things easier
      and leaves the recursive logic completely within the recursive function, and doesn't need to be duplicated at the main function
    
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(inorder) - 1
        pre_idx = 0
        map: Dict[int, int] = {}
        for i in range(0, len(inorder)) :
            map[inorder[i]] = i

        dummy = TreeNode()

        self.bt_helper(preorder, inorder, map, pre_idx, start, end, dummy, "left")

        return dummy.left

    def bt_helper(self, preorder: List[int], inorder:List[int], map: Dict[int, int], pre_idx: int, start:int, end:int, parent: TreeNode, branch: str):
        if pre_idx >= len(preorder):
            return
        
        if start > end:
            return
        
        root_val = preorder[pre_idx]
        root_idx = map[root_val]
        
        if start <= root_idx and end >= root_idx:
            root_node = TreeNode(val=root_val)
            if branch == "left":
                parent.left = root_node
            elif branch == "right":
                parent.right = root_node
            
            left_sub_tree_size = root_idx - start
            if left_sub_tree_size > 0:
                self.bt_helper(preorder, inorder, map, pre_idx + 1, start, root_idx - 1, root_node, "left")

            right_sub_tree_size = end - root_idx
            if right_sub_tree_size > 0:
                self.bt_helper(preorder, inorder, map, pre_idx + 1 + left_sub_tree_size, root_idx + 1, end, root_node, "right")