# Definition for singly-linked list.
from typing import Optional
"""

82. Remove Duplicates from Sorted List II

Medium

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:
[1] -> [2] -> [3] -> [3] -> [4] -> [4] -> [5]

[1] -> [2] -> [5]

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

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
    essentially two pointers.

    create a dummy list node that points to head to handle the edge case where the head node gets deleted

    create the first pointer node prev, initialize to be same as dummy node

    create another pointer node probe, that starts with head

    at each step, check if probe node's val equals the probe.next node's val, if so, advance probe until either the val changes, or run out of nodes, and then connect prev.next to probe
    else if probe node's val != probe.next node's val, then set prev to be probe, and advane probe
    
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        dummy:ListNode = ListNode()
        dummy.next = head
        prev = dummy
        probe = head

        while probe:
            if probe.next and probe.next.val == probe.val:
                mark = probe.val
                probe = probe.next
                while probe and probe.val == mark:
                    probe = probe.next
                prev.next = probe
            else:
                prev = probe
                probe = probe.next
        
        return dummy.next
        