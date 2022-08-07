package Contest;

public class NumberOfArithmeticTriplets {

    public static void main(String[] args) {
        int[] arr = { 0, 1, 4, 6, 7, 10 };
        System.out.println(arithmeticTriplets(arr, 3));
    }

    public static int arithmeticTriplets(int[] nums, int diff) {
        int count = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + diff == nums[j] && nums[j] + diff == nums[k]) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
