package Easy;

public class SearchInsertPosition {

    public static void main(String[] args) {
        int[] nums = { 1, 3 };
        int target = 2;

        System.out.println(searchInsert(nums, target));
        ;
    }

    public static int searchInsert(int[] nums, int target) {
        // binary search
        int firstIndex = 0;
        int lastIndex = nums.length - 1;
        while (true) {
            int mid = (firstIndex + lastIndex) / 2;
            if (target < nums[0]) {
                return 0;
            } else if (target > nums[lastIndex]) {
                return lastIndex + 1;
            } else if (target == nums[mid]) {
                return mid;
            }
            // else if (nums[mid - 1] < target && target < nums[mid]) {
            // return mid;
            // }
            else if (target < nums[mid]) {
                lastIndex = mid - 1;
            } else if (target > nums[mid]) {
                firstIndex = mid + 1;
            } else {
                return mid;
            }
        }

    }
}
