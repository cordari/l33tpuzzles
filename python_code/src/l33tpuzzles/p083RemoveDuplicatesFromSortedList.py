# Definition for singly-linked list.
from typing import Optional

"""
83. Remove Duplicates from Sorted List

Easy

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    pretty straight-forward 2 pointer algorithm

    a handle pointer stays behind, initialized to head, because the head node will never be a duplicate

    a probe pointer stays in front, initialized to the node after head.  at each step, check if the probe node value equals handle node value. if equal they are duplicates, advance probe to next
    and set handle.next to the advanced probe node.  if not equal, advance both handle and probe
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        handle = head
        probe = head.next

        while probe:
            if probe.val == handle.val:
                probe = probe.next
                handle.next = probe
            else:
                handle = probe
                probe = probe.next

        return head