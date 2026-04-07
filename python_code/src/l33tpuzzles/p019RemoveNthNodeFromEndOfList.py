"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:
[1] -> [2] -> [3] -> #4# -> [5]
    |
    V
[1] -> [2] -> [3] -> [5]

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    """
    keep two pointers, front and back.

    front would traverse the list n nodes, before both front and back traverse. This way, the back pointer always points to the node
    before the nth from the front. So when front reaches the end of the list, back points to the node before the one to be removed.

    before starting front and back, create a dummy node that points to the head. This would nicely handle the edge case where the head
    node is to be removed
    
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(val=0, next=head)
        fast: ListNode = dummy
        slow: ListNode = dummy

        result = head

        for i in range(0, n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next

        if slow.next == head:
            result = head.next
        else:
            slow.next = slow.next.next
        
        return result

def main():
    input = [1,2]
    head: ListNode = None
    current: ListNode = head
    for v in input:
        node = ListNode(val=v)
        if not head:
            head = node
        if not current:
            current = node
        else:
            current.next = node
            current = current.next

    check = head
    while check:
        print(check.val)
        check = check.next
    
    sol = Solution()
    ans = sol.removeNthFromEnd(head, 2)

    hd = ans
    while hd:
        print(hd.val)
        hd = hd.next

if __name__ == "__main__":
    main()
