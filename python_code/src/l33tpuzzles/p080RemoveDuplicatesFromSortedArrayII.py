
from typing import List
"""

80. Remove Duplicates from Sorted Array II

Medium

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
"""

class Solution:
    """
    realization is that k tracks the number of deduped elements so far in the array, and it also indicates the vacant position occupied by a duplicate if k lags behind the probe index i, so probe finds
    a non-duplicate, it should be copied to the position at k

    initialize the marker element to the first element of the array since the first element cannot be a duplicate, and set element count to 1.  initialize k to 1 to indicate the first element is
    always valid

    loop through the rest of the elements in the array

    if the current element matches the marker, increment the element count; otherwise, set the marker to be the current element and reset count to 1

    when element count is less than or equal to 2, the element is valid, and check to see if it needs to be copied to where k is. copy it if k is lagging behind i.

    technically you could blindly copy it to num[k], because when k is not lagging behind i, it would be equal to i, so the copy would make no difference. 

    advance k if the element count is less than or equal 2.

    
    An even more clever way:
    initialize k = 2 as the first two elements are always valid; loop through element index 2 to the end.  if element[i] != element[k-2], then element[i] is valid, copy to [k] position, advance k.
        if element[i] == element[k-2], it is a duplicate, skip it.

    """
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        elem = nums[0]
        elem_count = 1

        i = 1

        while i < len(nums):
            v = nums[i]
            if v == elem:
                elem_count += 1
            else:
                elem = v
                elem_count = 1

            if elem_count <= 2:
                if k < i:
                    nums[k] = v
                k += 1
            i += 1
        return k

def main():
    nums = [1,1,1,2,2,3]
    nums =[0,0,1,1,1,1,2,3,3]
    nums = [0,1,1,1,1,1]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(nums)

main()
                