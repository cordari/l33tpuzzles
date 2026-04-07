# Definition for singly-linked list.
from typing import Optional

"""
2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

"""
this works just like how we learned to do addition by hand. since the lists are reversed, the first number is the least significant
digit, and so on.

key challenges are:
1. handle when one list is exhausted, but the other is not
2. keep a carry. when both lists are exhausted, if the carry is > 0, the final answer list needs another element

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ended: bool = l1 is None
        l2_ended: bool = l2 is None

        lst1 = l1
        lst2 = l2
        
        sum_list = ListNode(val=0)
        sum_curr_digit = sum_list

        carry: int = 0

        while (not (l1_ended and l2_ended)) or carry != 0:
            digit_sum: int = carry
            carry = 0
            d1: int = 0 if l1_ended else lst1.val
            d2: int = 0 if l2_ended else lst2.val
            digit_sum: int = digit_sum + d1 + d2
            sum_curr_digit.val = digit_sum % 10
            carry = digit_sum // 10

            if not l1_ended:
                lst1 = lst1.next

            if not l2_ended:
                lst2 = lst2.next

            l1_ended = lst1 is None
            l2_ended = lst2 is None

            if (not (l1_ended and l2_ended)) or carry != 0:
                sum_curr_digit.next = ListNode(val=0)
                sum_curr_digit = sum_curr_digit.next
        
        return sum_list
            
