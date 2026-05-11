
from typing import List, Optional
"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.

"""
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    the trick of this problem is knowing to use a priority queue / min-heap to hold the current nodes of all k lists
    and it guarantees to pop the one with the minimum.

    after the heap is initialized with the head nodes of each list, you don't even need to track the current nodes of 
    these lists. because when you pop off a node from the min-heap, you should push the next node onto the min-heap,
    and that next node is pointed at by the .next of the node you just poppped off.

    it is more challenging to know how to use python (or whatever language)'s min-heap, which is from heapq, and also
    knowing some behaviors 

    given a list a = [1,2,3,4], you can heapfy it by:
    heapq.heapfy(a)

    to push an element
    heapq.heappush(a, item)

    and to pop an element
    e = heapq.heappop(a)

    for item, it is usually a tuple. typicall it would be (priority, data), where priority is used by heapq
    for comparison.  BUT, when there is a tie on priority, it would use the second element for comparison.
    if we put the ListNode as the second element, it would crash. So instead, we use a 3-tuple for the item:
    (priority, list id, ListNode), where priority is the val of the ListNode, and list id is which of the k
    lists this node is from, so it can be the tie breaker
    
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        merged_list: ListNode = None
        merged_curr: ListNode = None
        min_heap = []
        heapq.heapify(min_heap)

        for i in range(0, k):
            l = lists[i]
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        while len(min_heap) > 0:
            min_tuple = heapq.heappop(min_heap)
            if not merged_list:
                merged_list = min_tuple[2]
                merged_curr = min_tuple[2]
            else:
                merged_curr.next = min_tuple[2]
                merged_curr = merged_curr.next
            if min_tuple[2].next:
                heapq.heappush(min_heap, (min_tuple[2].next.val, min_tuple[1], min_tuple[2].next))

        return merged_list



        