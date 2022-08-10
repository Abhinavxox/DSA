package Easy;

import java.util.Arrays;

public class PlusOne {

    public static void main(String[] args) {
        int digits[] = { 9, 9 };
        System.out.println(Arrays.toString(plusOne(digits)));
    }

    public static int[] plusOne(int[] digits) {
        if (digits.length == 1 && digits[0] == 9) {
            int[] result = { 1, 0 };
            return result;
        }
        digits[digits.length - 1] += 1;
        if (digits[digits.length - 1] == 10) {
            for (int i = digits.length - 1; i >= 0; i--) {
                // worst corner case
                // 10000000...
                if (digits[0] == 10) {
                    int[] newArr = new int[digits.length + 1];
                    newArr[0] = 1;
                    for (int j = 1; j < newArr.length; j++) {
                        newArr[j] = 0;
                    }
                    return newArr;
                }

                if (digits[i] == 10) {
                    digits[i - 1] += 1;
                    digits[i] = 0;
                } else {
                    return digits;
                }
            }
            return digits;
        } else {
            return digits;
        }

    }
}
