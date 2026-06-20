# Definition for singly-linked list.
from typing import List, Optional

"""
61. Rotate List

Medium

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
          [1] -> [2] -> [3] -> [4] -> [5]
rotate 1: [5] -> [1] -> [2] -> [3] -> [4]
rotate 2: [4] -> [5] -> [1] -> [2] -> [3]

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


Example 2:
              [0] -> [1] -> [2]
rotate 1:     [2] -> [0] -> [1]
rotate 2:     [1] -> [2] -> [0]
rotate 3:     [0] -> [1] -> [2]
rotate 4:     [2] -> [0] -> [1]


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    ring algorithm:
    1. traverse the entire list to get number of nodes, also reach the tail
     and connect tail to the head to form a ring

    2. number of rotations modulo number of nodes to avoid redundant
    full cycles

    3. find where the cut should be, and disconnect. to find the cut, 
    use number of nodes minus the modulo rotate, this gives how many times the
    tail should move. it will land on the node before the cut (i.e the tail node after cut),
    grab the node.next which would be the new head, and then set node.next = None to cut
    
    """
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        tail: ListNode = head
        node_count = 1
        while tail.next:
            node_count += 1
            tail = tail.next

        tail.next = head  # connect to form a ring
        rotate = k % node_count
        move = node_count - rotate

        for i in range(0, move):
            tail = tail.next
        
        new_head = tail.next
        tail.next = None

        return new_head
    
    """
    stack algorithm:
    1. traverse the entire list to get number of nodes, but also put each node onto a stack, 
    also keep a tail pointer
    2. compute modulo of rotation vs num of nodes to avoid redundant full cycles
    3. if modulo rotation is 0, return head; otherwise, pop modulo rotation number of nodes
    off the stack. the last node popped off is the new head. connect tail to head, and set
    stack top's next to None. return the new head.

    One caveat: make sure all nodes are pushed to the stack. in this implementation, there is 
    a final stack.append(tail) after the loop

    """
    def rotateRight_stack(self, head:Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        tail: ListNode = head
        stack: List[ListNode] = []
        node_count = 1
        while tail.next:
            stack.append(tail)
            tail = tail.next
            node_count += 1
        stack.append(tail)

        rotate = k % node_count
        if rotate == 0:
            return head
        
        new_head = None
        for i in range(0, rotate):
            new_head = stack.pop()
        
        stack_top = stack.pop()
        stack_top.next = None
        tail.next = head

        return new_head
    