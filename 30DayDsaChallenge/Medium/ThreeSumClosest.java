package Medium;

import java.util.ArrayList;
import java.util.Collections;

public class ThreeSumClosest {

    public static void main(String[] args) {
        int[] nums = { 1, 1, 1, 0 };
        System.out.println(threeSumClosest(nums, 100));
        ;
    }

    public static int threeSumClosest(int[] nums, int target) {
        ArrayList<Integer> sums = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    break;
                }
                for (int k = 0; k < nums.length; k++) {
                    if (k == i || k == j) {
                        break;
                    }
                    int sum = nums[i] + nums[j] + nums[k];
                    if (sum == target) {
                        return target;
                    }
                    if (!sums.contains(sum)) {
                        sums.add(sum);
                    }
                }
            }
        }
        if (sums.size() == 1) {
            return sums.get(0);
        }
        sums.add(target);
        Collections.sort(sums);
        if (sums.indexOf(target) == 0) {
            return sums.get(1);
        }
        if (sums.indexOf(target) == sums.size() - 1) {
            return sums.get(sums.size() - 2);
        }
        int lower = sums.get(sums.indexOf(target) - 1);
        int higher = sums.get(sums.indexOf(target) + 1);
        if (higher - target > target - lower) {
            return lower;
        }
        return higher;
    }
}
