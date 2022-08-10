package Medium;

public class IntegerToRoman {

    public static void main(String[] args) {
        System.out.println(intToRoman(3));
        ;
    }

    public static String intToRoman(int num) {
        String[] romanLiterals = { "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
        int[] correspondingIntgers = { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
        int i = 0;
        StringBuilder roman = new StringBuilder();
        while (num > 0) {
            if (num == 1) {
                roman.append("I");
                break;
            }

            if (correspondingIntgers[i] <= num) {
                roman.append(romanLiterals[i]);
                num -= correspondingIntgers[i];
            } else {
                i++;
            }
        }
        return roman.toString();
    }
}
