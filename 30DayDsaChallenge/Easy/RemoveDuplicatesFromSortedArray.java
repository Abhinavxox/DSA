package Easy;
import java.util.ArrayList;

public class RemoveDuplicatesFromSortedArray {

    public int removeDuplicates(int[] nums) {
        ArrayList<Integer> alist = new ArrayList<>();
        for (int x : nums) {
            if (!alist.contains(x)) {
                alist.add(x);
            }
        }
        for (int i = 0; i < alist.size(); i++) {
            nums[i] = alist.get(i);
        }
        return alist.size();

    }

}
