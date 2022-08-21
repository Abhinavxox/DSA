package Easy;

import java.util.ArrayList;

public class SingleNumber {

    public static void main(String[] args) {
        int[] nums = { 2, 2, 1 };
        System.out.println(singleNumber(nums));

        System.out.println(Math.abs(-2147483648));
    }

    public static int singleNumber(int[] nums) {
        ArrayList<Integer> alist = new ArrayList<>();
        for (int x : nums) {
            if (!alist.contains(x)) {
                alist.add(x);
            } else {
                alist.remove(alist.indexOf(x));
            }
        }
        return alist.get(0);
    }
}
