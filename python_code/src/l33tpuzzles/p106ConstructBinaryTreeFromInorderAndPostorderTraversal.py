# Definition for a binary tree node.
from typing import Dict, List, Optional
"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

           [3]
          /   \
       [9]     [20]
              /    \
          [15]      [7]

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Observations:
    1. in postorder list slice, the root is at the end of the list slice. The root of the entire tree is the very last node/element, so we should go from end of the list to the beginning on the post-order
    2. when you find the index of the root in the in-order list slice, everything to the right of the root index is the right subtree, and everything to the left of the root index is the left subtree
    3. if the root has right subtree (determined by the start and root index), the root of the right subtree is the element before the root element of the current level on the postorder list
    4. if the root has left subtree (determined by the root index and end), the index of the root of the left subtree is index of current root - right subtree size - 1 on the postorder list


    algorithm:
    1. the root value is the postorder element at the passed-in post_idx
    2. find the root index within the in-order list
    3. everything to the right of root index in the in-order slice is the right subtree of the current root
    4. everything to the left of the root index in the in-order slice is the left subtree of the current root
    5. create a treenode to hold the root value, and attach it to the passed-in parent node using the passed-in direction
    6. if the root has right subtree, recursive call with post_idx - 1
    7. if the root has left subtree, recursive call with post_idx - right subtree size - 1
    8. terminal condition: if post_idx < 0, or if the root index from in-order list is out size of the passed-in start and end

    9. to make things easier. at the main function, create a dummy root, so the actual root of the tree would be a child of the dummy root. this makes things easier as all the recursive logic
      resides in the recursive function, without the need to repeat some processing logic in the main function itself. when done, return the child of dummy 


    NOTE: in this implementation, it choose start >= end to go backwards from the postorder list. It is not always necessary. 
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        start = len(postorder) - 1
        end = 0
        post_idx = len(postorder) - 1

        map: Dict[int, int] = {}

        for i in range(0, len(inorder)):
            map[inorder[i]] = i

        dummy = TreeNode()

        self.bt_helper(inorder, postorder, post_idx, start, end, map, dummy, "right")

        return dummy.right

    def bt_helper(self, inorder: List[int], postorder: List[int], post_idx: int, start: int, end: int, map:Dict[int, int], parent: TreeNode, dir: str):
        if post_idx < 0:
            return
        
        root_val = postorder[post_idx]
        root_idx = map[root_val]

        # start >= end as we are going from back of inorder list
        if root_idx > start or root_idx < end:
            return
        
        root_node = TreeNode(val = root_val)
        if dir == "left":
            parent.left = root_node
        elif dir == "right":
            parent.right = root_node

        right_sub_tree_size = start - root_idx
        if right_sub_tree_size > 0:
            self.bt_helper(inorder, postorder, post_idx - 1, start, root_idx + 1, map, root_node, "right")

        left_sub_tree_size = root_idx - end
        if left_sub_tree_size:
            self.bt_helper(inorder, postorder, post_idx - right_sub_tree_size - 1, root_idx - 1, end, map, root_node, "left")
