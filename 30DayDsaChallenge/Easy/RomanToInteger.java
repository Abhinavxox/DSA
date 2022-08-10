package Easy;

import java.util.ArrayList;
import java.util.Arrays;

public class RomanToInteger {

    public static void main(String[] args) {
        System.out.println(romanToInt("MCMXCIV"));
    }

    public static int romanToInt(String s) {
        ArrayList<String> romanLiterals = new ArrayList<>(
                Arrays.asList("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"));
        int[] correspondingIntgers = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        int result = 0;
        int i = 0;
        while (i != s.length()) {
            String test = "";
            try {
                test = s.substring(i, i + 2);
            } catch (Exception e) {
            }
            if (romanLiterals.contains(test)) {
                result += correspondingIntgers[romanLiterals.indexOf(test)];
                i += 2;
            } else {
                result += correspondingIntgers[romanLiterals.indexOf(String.valueOf(s.charAt(i)))];
                i++;
            }
        }
        return result;
    }
}
