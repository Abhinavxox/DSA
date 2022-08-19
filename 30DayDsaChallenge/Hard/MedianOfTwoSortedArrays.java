package Hard;

import java.util.Arrays;

public class MedianOfTwoSortedArrays {

    public static void main(String[] args) {
        int[] nums1 = {};
        int[] nums2 = { 2, 3 };
        System.out.println(findMedianSortedArrays(nums1, nums2));
        ;
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int arr[] = new int[m + n];
        int j = 0, k = 0;

        if (m == 0 && n == 0) {
            return 0;
        } else if (m == 0) {
            if (n % 2 != 0) {
                return nums2[(n - 1) / 2];
            } else {
                double result = nums2[(n / 2)] + nums2[(n / 2 - 1)];
                return result / 2;
            }
        } else if (n == 0) {
            if (m % 2 != 0) {
                return nums1[(m - 1) / 2];
            } else {
                double result = nums1[(m / 2)] + nums1[(m / 2 - 1)];
                return result / 2;
            }
        }
        int pointer = 0;
        while (true) {
            if (j == m) {
                while (k != n) {
                    arr[pointer] = nums2[k];
                    pointer++;
                    k++;
                }
                break;
            } else if (k == n) {
                while (j != m) {
                    arr[pointer] = nums1[j];
                    pointer++;
                    j++;
                }
                break;
            } else if (nums1[j] <= nums2[k]) {
                arr[pointer] = nums1[j];
                j++;
            } else {
                arr[pointer] = nums2[k];
                k++;
            }
            pointer++;
        }
        System.out.println(Arrays.toString(arr));

        int l = arr.length;
        if (l % 2 != 0) {
            return arr[(l - 1) / 2];
        } else {
            double result = arr[(l / 2)] + arr[(l / 2 - 1)];
            return result / 2;
        }

    }

}
