package Easy;

import java.util.Arrays;

public class MergeSortedArray {
    public static void main(String[] args) {
        int[] nums1 = { -1, 0, 0, 3, 3, 3, 0, 0, 0 };
        int m = 6;
        int n = 3;
        int[] nums2 = { 1, 2, 2 };
        System.out.println(Arrays.toString(merge(nums1, m, nums2, n)));
    }

    public static int[] merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[m + n];
        int j = 0, k = 0;
        int pointer = 0;
        if (n == 0) {
            return nums1;
        }
        while (true) {
            if (j + k == m + n) {
                break;
            } else if (k == n - 1 && nums1[j] > nums2[k]) {
                temp[pointer] = nums2[k];
                k++;
                pointer++;
                while (j != m) {
                    temp[pointer] = nums1[j];
                    pointer++;
                    j++;
                }
            } else if (nums1[j] <= nums2[k] && j != m) {
                temp[pointer] = nums1[j];
                pointer++;
                j++;
            } else {
                temp[pointer] = nums2[k];
                pointer++;
                k++;
            }
        }
        for (int i = 0; i < nums1.length; i++) {
            nums1[i] = temp[i];
        }
        return nums1;
    }
}
