package Easy;

import java.util.Deque;
import java.util.LinkedList;

public class ValidPalindrome {

    public static void main(String[] args) {
        System.out.println(isPalindrome("race a car"));
    }

    public static boolean isPalindrome(String s) {
        // for (int i = 0; i < s.length(); i++) {
        // if (Character.isLetterOrDigit(s.charAt(i))) {
        // try {
        // if (Character.isLetterOrDigit(s.charAt(i))) {
        // if (checker.isEmpty()) {
        // checker.add(s.charAt(i));
        // } else {
        // if ((char) checker.peek() == s.charAt(i)) {
        // checker.pop();
        // } else {
        // checker.add(s.charAt(i));
        // }
        // }
        // }
        // } catch (Exception e) {
        // }
        // }
        // }
        // if (checker.isEmpty()) {
        // return true;
        // } else {
        // return false;
        // }
        Deque llist = new LinkedList<Character>();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                llist.add(Character.toLowerCase(s.charAt(i)));
            }
        }
        boolean flag = true;
        while (llist.size() > 1) {
            if (llist.removeFirst() != llist.removeLast()) {
                flag = false;
            }
        }
        return flag;
    }

}
