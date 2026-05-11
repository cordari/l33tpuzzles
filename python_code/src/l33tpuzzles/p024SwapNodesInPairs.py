# Definition for singly-linked list.
from typing import Optional

"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 [1] -> [2] -> [3] -> [4]
           |
           v
 [2] -> [1] -> [4] -> [3]



Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
no trick, just need to have clear picture of moving pointers.

keep 5 pointers, current, current_plus, next, next_plus, and prev

current points to 1, current_plus points to 2, next points to 3, and next_plus points to 4.  prev is initially None

swap current and current_plus

advance current and current_plus to next and next_plus, and advance next and next_plus. also remember to update prev.next and advance prev as well

"""
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        curr: ListNode = head
        curr_plus: ListNode = head.next
        next: ListNode = curr_plus.next
        next_plus: ListNode = next.next if next else None
        prev: ListNode = None
        ans: ListNode = curr_plus

        while curr and curr_plus:
            curr_plus.next = curr
            curr.next = next
            if prev:
                prev.next = curr_plus
            
            prev = curr
            curr = next
            curr_plus = next_plus
            next = curr_plus.next if curr_plus else None
            next_plus = next.next if next else None

        return ans

def main():
    input = []

    input_head: ListNode = None
    curr:ListNode = None
    for i in input:
        node: ListNode = ListNode(val = i)

        if not input_head:
            input_head = node
            curr = input_head
        else:
            curr.next = node
            curr = node

    curr = input_head

    print("Input")
    while curr:
        print(curr.val)
        curr = curr.next


    sol = Solution()

    output_head: ListNode = sol.swapPairs(input_head)

    output_curr = output_head
    
    print("Output")
    while output_curr:
        print(output_curr.val)
        output_curr = output_curr.next

if __name__ == "__main__":
    main()



