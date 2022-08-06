package Easy;

import java.util.ArrayList;

public class RemoveElement {
    public int removeElement(int[] nums, int val) {
        ArrayList<Integer> alist = new ArrayList<>();
        for (int x : nums) {
            if (x != val) {
                alist.add(x);
            }
        }

        for (int i = 0; i < alist.size(); i++) {
            nums[i] = alist.get(i);
        }

        return alist.size();

    }
}
