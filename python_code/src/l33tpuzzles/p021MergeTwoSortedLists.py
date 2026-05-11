

# Definition for singly-linked list.
from typing import Optional

"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 [1] -> [2] -> [4]
 [1] -> [3] -> [4]

 [1] -> [1] -> [2] -> [3] -> [4] -> [4]

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    quite straight-forward - take the node with the smaller value to merge.

    1. handle the remaining list when one list ends first.
    2. got-you: when handling the remaining list, also need to check if the merged list head is still None, because the original input could have an empty list to begin with
    
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ended = list1 == None
        l2_ended = list2 == None

        l1_curr = list1
        l2_curr = list2

        result = None
        result_curr = None

        while not (l1_ended or l2_ended):
            node = None
            if l1_curr.val <= l2_curr.val:
                node = l1_curr
                l1_curr = l1_curr.next
                l1_ended = l1_curr == None
            else:
                node =l2_curr
                l2_curr = l2_curr.next
                l2_ended = l2_curr == None
            if not result:
                result = node
                result_curr = node
            else:
                result_curr.next = node
                result_curr = result_curr.next
        
        remain: ListNode = None
        if not l1_ended:
            remain = l1_curr
        elif not l2_ended:
            remain = l2_curr

        if remain:
            if not result:
                result = remain
            else:
                result_curr.next = remain
        
        return result
    
def main():
    input1 = [1,2,4] #[1,2,4]
    input2 = [1,3,4] # [1,3,4]

    l1: ListNode = None
    l1_curr: ListNode = None
    for e1 in input1:
        node = ListNode(val=e1)
        if l1 == None:
            l1 = node
            l1_curr = node
        else:
            l1_curr.next = node
            l1_curr = node

    l2: ListNode = None
    l2_curr: ListNode = None
    for e2 in input2:
        node = ListNode(val=e2)
        if l2 == None:
            l2 = node
            l2_curr = node
        else:
            l2_curr.next = node
            l2_curr = node
    
    print("input1")
    print_list(l1)
    print("input2")
    print_list(l2)

    sol = Solution()
    res = sol.mergeTwoLists(l1, l2)
    print("result")
    print_list(res)

def print_list(list: ListNode):
    if not list:
        print("[]")
    h = list
    while h:
        print(h.val)
        h = h.next

if __name__ == "__main__":
    main()