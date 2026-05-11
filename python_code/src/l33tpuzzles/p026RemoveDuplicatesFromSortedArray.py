from typing import List
"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

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

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 1^04
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

"""

class Solution:
    """
    quite straight forward.
    first number is always unique by itself.
    keep an anchor point to the latest unique number at its index (start at 0 as it points to the first number initially)
    keep a counter of number of unique numbers (start with 1)

    go through the rest of the array. when a value differs from the value at anchor, another unique number is found. increment
    the unique counter, increment the anchor index, and copy the new unique value to the new anchor index in the array
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 1
        anchor_idx = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[anchor_idx]:
                unique_count += 1
                anchor_idx += 1
                nums[anchor_idx] = nums[i]

        return unique_count
    
def main():
    input = [1,2,2,2,2,2,2,2,2,2,3]
    sol = Solution()
    k = sol.removeDuplicates(input)

    print(k)
    print(input)

if __name__ == "__main__":
    main()


