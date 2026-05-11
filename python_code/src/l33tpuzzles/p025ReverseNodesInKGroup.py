# Definition for singly-linked list.
from typing import List, Optional

"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

[1] -> [2] -> [3] -> [4] -> [5]
             |
             v
[2] -> [1] -> [4] -> [3] -> [5]
 

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


Example 2:

[1] -> [2] -> [3] -> [4] -> [5]

[3] -> [2] -> [1] -> [4] -> [5]


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
similar to the swap nodes in pairs, just generalized. 

need to watch out for edge cases, where the general while loop in the middle is never executed, and there needs to be a check to see if there are
still k nodes left outside of the loop, if so, they need to be reversed. if less than k, then nothing to be done.  But if there are k nodes
left, the "ans" could also be None if the while loop was never executed.
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        ans: ListNode = None
        prev: ListNode = None
        # curr_ptr: ListNode = head
        curr_nodes: List[ListNode] = []
        next_ptr: ListNode = head

        for i in range(0, k):
            curr_nodes.append(next_ptr)
            next_ptr = next_ptr.next
            if not next_ptr:
                break
        
        if len(curr_nodes) < k:
            return head
        

        while next_ptr:
            if not ans:
                ans = curr_nodes[-1]
            for i in range(k-1, 0, -1):
                curr_nodes[i].next = curr_nodes[i-1]
            curr_nodes[0].next = next_ptr
            if prev:
                prev.next = curr_nodes[-1]

            prev = curr_nodes[0]
            
            curr_nodes.clear()

            for i in range(0, k):
                curr_nodes.append(next_ptr)
                next_ptr = next_ptr.next
                if not next_ptr:
                    break

        if len(curr_nodes) == k:
            if not ans:
                ans = curr_nodes[-1]
            for i in range(k-1, 0, -1):
                curr_nodes[i].next = curr_nodes[i-1]
            curr_nodes[0].next = next_ptr
            if prev:
                prev.next = curr_nodes[-1]

        return ans
    
def main():
    input = [1,2,3,4,5,6,7,8,9,10,11,12]
    k = 5
    input_hd: ListNode = None
    input_curr: ListNode = None
    for e in input:
        node = ListNode(val = e)
        if not input_hd:
            input_hd = node
            input_curr = input_hd
        else:
            input_curr.next = node
            input_curr = node

    print("input")
    input_curr = input_hd
    while input_curr:
        print(input_curr.val)
        input_curr = input_curr.next


    sol = Solution()

    output: ListNode = sol.reverseKGroup(input_hd, k)

    output_curr = output
    print("output")
    while output_curr:
        print(output_curr.val)
        output_curr = output_curr.next



if __name__ == "__main__":
    main()




