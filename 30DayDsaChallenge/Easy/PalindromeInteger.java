package Easy;

import java.util.LinkedList;

public class PalindromeInteger {
    public static void main(String[] args) {
        System.out.println(isPalindrome(11));
    }

    public static boolean isPalindrome(int x) {
        String y = String.valueOf(x);
        LinkedList llist = new LinkedList<Character>();
        for (int i = 0; i < y.length(); i++) {
            llist.add(y.charAt(i));
        }
        boolean isPalindrome = false;
        while (true) {
            if (llist.size() <= 1) {
                isPalindrome = true;
                break;
            }
            if (llist.removeFirst() == llist.removeLast()) {
                continue;
            } else {
                isPalindrome = false;
                break;
            }

        }
        return isPalindrome;
    }
}
