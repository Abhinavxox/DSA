package Medium;

public class StringToIntegerATOI {

    public static void main(String[] args) {
        System.out.println(myAtoi(""));
        ;
    }

    public static int myAtoi(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        StringBuilder returnValue = new StringBuilder();
        int pointer = 0;
        // check leading white spaces
        while (s.charAt(pointer) == ' ') {
            pointer++;
            if (checkEnd(pointer, s)) {
                return 0;
            }
        }

        // check for + or -
        if (s.charAt(pointer) == '+' || s.charAt(pointer) == '-') {
            returnValue.append(s.charAt(pointer));
            pointer++;
            if (checkEnd(pointer, s)) {
                return 0;
            }
        }

        // read until non digit char is found
        if (!Character.isDigit(s.charAt(pointer))) {
            return 0;
        }
        while (Character.isDigit(s.charAt(pointer))) {
            returnValue.append(s.charAt(pointer));
            pointer++;
            if (checkEnd(pointer, s)) {
                break;
            }
        }

        // number format
        try {
            return Integer.parseInt(returnValue.toString());
        } catch (NumberFormatException e) {
            if (Double.parseDouble(returnValue.toString()) < Math.pow(-2, 31)) {
                return Integer.MIN_VALUE;
            }
            return Integer.MAX_VALUE;
        }
    }

    public static boolean checkEnd(int pointer, String s) {
        if (pointer >= s.length()) {
            return true;
        }
        return false;
    }
}
