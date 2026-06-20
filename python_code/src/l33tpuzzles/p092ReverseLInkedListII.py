# Definition for singly-linked list.
from typing import Optional
"""
92. Reverse Linked List II

Medium

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:
[ 1 ] -> [.2.] -> [.3.] -> [.4.] -> [ 5 ]

                  |
                  v
[ 1 ] -> [.4.] -> [.3.] -> [.2.] -> [ 5 ] 

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    create a dummy node whose next points to head, to make things easier

    another reverse dummy node whose next points to the reversed section

    a pointer that will point to the tail of the reversed section

    two more pointers - a probe in the front, with a handle stay in the back. handle initially is the first dummy node, it will stop at the node before the first node to be reversed.

    the probe node initialized to be the head and will stop when it reaches the first node after the last node to be reversed

    everytime probe sees a node to be reversed, it inserts between the reverse dummy node and reverse dummy node.next.  for the first node added to the reverse section, set reverse tail to it


    after probe sees all the nodes to be reversed, connect handle.next to reverse dummy node.next
    connect reverse tail.next to be probe

    return dummy node.next
    
    """
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        dummy: ListNode = ListNode()
        dummy.next = head

        handle = dummy
        probe = head
        probe_pos = 1

        reverse: ListNode = ListNode()
        reverse_tail: Optional[ListNode] = None

        while probe and probe_pos <= right:
            if probe_pos >= left and probe_pos <= right:
                copy = probe
                probe = probe.next
                probe_pos += 1
                copy.next = reverse.next
                reverse.next = copy
                if not reverse_tail:
                    reverse_tail = copy
            else:
                probe = probe.next
                probe_pos += 1
                handle = handle.next

        handle.next = reverse.next
        reverse_tail.next = probe

        return dummy.next



