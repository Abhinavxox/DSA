package Medium;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class ThreeSum {
    static HashMap<ArrayList<Integer>, Integer> check = new HashMap<>();

    public static void main(String[] args) {
        int[] nums = { -1, 0, 1, 2, -1, -4 };
        System.out.println(threeSum(nums));
        System.out.println(check);
    }

    public static List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> toReturn = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    break;
                }
                for (int k = 0; k < nums.length; k++) {
                    if (k == i || k == j) {
                        break;
                    }
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        ArrayList<Integer> temp = new ArrayList<>();
                        temp.add(i);
                        temp.add(j);
                        temp.add(k);
                        if (!check.containsKey(temp)) {
                            check.put(temp, 0);
                            List<Integer> alist = new ArrayList<>();
                            alist.add(nums[i]);
                            alist.add(nums[j]);
                            alist.add(nums[k]);
                            toReturn.add(alist);
                        }
                    }
                }
            }
        }
        return toReturn;
    }
}
