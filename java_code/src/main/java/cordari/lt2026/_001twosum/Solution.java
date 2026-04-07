import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 1. Two Sum
 * 
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 * 
 * Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 */
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
          naive solution, O(n^2)
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[]{-1, -1};
        */ 


        /* 
        uses hashmap, but not optimized, as it goes through the list twice
        which is unnecessary

        final Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            final int value = nums[i];
            final List<Integer> list = map.get(value);
            if (list == null) {
                final List<Integer> l = new ArrayList<>();
                l.add(i);
                map.put(value, l);
            } else {
                list.add(i);
            }
        }

        for (int i = 0; i < nums.length - 1; i++) {
            final int diff = target - nums[i];
            final List<Integer> list = map.get(diff);
            if (list != null) {
                final int index = list.getFirst();
                if (index != i) {
                    // if second index is different from first index, return both
                    return new int[] {i, index};
                } else {
                    // edge case where first value and second value are equal and sum to target, then they would land on the same list
                    // and we need to make sure the list has more than 1 element. if so, return; if not, then we have to move on
                    if (list.size() > 1) {
                        return new int[] {i, list.get(1)};
                    }
                }
            }
        }
        return new int[]{-1, -1};
        */


        final Map<Integer, List<Integer>> valueToIndexMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            final int delta = target - nums[i];
            final List<Integer> indices = valueToIndexMap.get(delta);
            if (indices != null) {
                return new int[]{i, indices.getFirst()};
            } else {
                final List<Integer> ind = new ArrayList<>();
                ind.add(i);
                valueToIndexMap.put(nums[i], ind);
            }
        }
        return new int[]{-1, -1};
    }

}
