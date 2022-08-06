import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        System.out.println(Arrays.toString(twoSum(nums, target)));
    }

    public static int[] twoSum(int[] nums, int target) {
        ArrayList<Integer> output = new ArrayList<>();
        int i = 0;
        boolean flag = true;
        while (flag) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                } else if ((nums[i] + nums[j]) == target) {
                    output.add(i);
                    output.add(j);
                    flag = false;
                    break;
                }
            }
            i++;
        }

        Collections.sort(output);
        int[] out = new int[output.size()];
        for (int x = 0; x < output.size(); x++) {
            out[x] = output.get(x);
        }
        return out;
    }
}