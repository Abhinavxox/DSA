package Medium;

public class ReverseInteger {

    public static int reverse(int x) {
        try {
            if (Math.pow(-2, 31) > x || x > Math.pow(2, 31)) {
                return 0;
            }
            boolean isNegative = false;
            if (x < 0) {
                isNegative = true;
            }
            StringBuilder sb = new StringBuilder(String.valueOf(Math.abs(x)));
            sb.reverse();

            if (isNegative) {
                return Integer.parseInt(sb.toString()) * (-1);
            }
            return Integer.parseInt(sb.toString());
        } catch (NumberFormatException e) {
            return 0;
        }
    }
}
