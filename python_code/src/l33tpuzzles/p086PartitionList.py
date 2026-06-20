# Definition for singly-linked list.
from typing import Optional
"""
86. Partition List

Medium

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:

[1] -> [4] -> [.3.] -> [2] -> [5] -> [2]

[1] -> [2] -> [2] -> [.3.] -> [4] -> [5]

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    create 2 lists, before and after, each with a dummy node at the front to make things easier

    pin the two dummy nodes with a before_handle and after_handle

    each list will also have a pointer to the last node, before_prev and after_prev. new nodes will be appened as .next of these pointer

    another probe to go through the original list.

    if probe val is less than target, append to before list, advance before_prev and probe; otherwise, appen to after list, advance after_prev and probe

    after probe goes through all nodes, connect before and after by setting before_prev.next = after_handle.next, and also terminate after_prev by setting its next to None

    return before_handle.next
    
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        before_handle: ListNode = ListNode()
        before_prev = before_handle
        after_handle: ListNode = ListNode()
        after_prev = after_handle

        probe = head
        while probe:
            if probe.val < x:
                before_prev.next = probe
                before_prev = before_prev.next
                probe = probe.next
            else:
                after_prev.next = probe
                after_prev = after_prev.next
                probe = probe.next

        before_prev.next = after_handle.next
        after_prev.next = None

        return before_handle.next
    