"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5

"""

class Solution:
    """
    this differs from the 2sum not only that it has 3 numbers, but also needs to find all distinct answers.

    the idea is:
    1. sort the array, making it easier to skip duplicate numbers, and also making it easier to binary search
    2. pin down the first number, and use binary search to find the other two numbers
    3. if a pair is found, don't stop, move left pointer as long as the number is the same as the previous left, and try to find additional pairs
    4. when binary search returns, form answers, and move the first number pointer to the right. similarly keep going if the new number is the same as the previous
    first number

    """
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answers = []
        nums.sort()
        pinned = 0
        while pinned < len(nums) - 2:
            if pinned == 0 or (pinned > 0 and nums[pinned] != nums[pinned - 1]):
                
                left = pinned + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[pinned] + nums[left] + nums[right]
                    if sum > 0:

                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            # move right pointer to the left, but skip all numbers that are the same
                            right -= 1
                        
                    elif sum < 0:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            # move left pointer to the right, but skipp all numbers that are the same
                            left += 1
                    else:
                        # found one answer
                        answers.append([nums[pinned], nums[left], nums[right]])
                        left += 1
                        # move left pointer to the right, but skip all the numbers that are the same
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
            pinned += 1

        return answers

def main():
    sol = Solution()
    print(sol.threeSum([0,0,0, 0, 0]))             

if __name__ == "__main__":
    main()
