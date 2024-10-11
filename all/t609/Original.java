import java.util.HashMap;

class Solution {

    //main generated with copilot
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        Solution sol = new Solution();
        int[] ret = sol.twoSum(nums, target);

        for (int i = 0; i < ret.length; i++) {
            System.out.println(ret[i]);
        }
    }

    //My work starts here
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            numsMap.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numsMap.containsKey(complement) && numsMap.get(complement) != i) {
                return new int[] { i, numsMap.get(complement) };
            }
        }

        throw new IllegalArgumentException("No two sum solution");
    }
}