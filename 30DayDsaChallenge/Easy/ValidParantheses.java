package Easy;

import java.util.HashMap;
import java.util.Stack;

public class ValidParantheses {

    public static void main(String[] args) {
        System.out.println(isValid("))"));
    }

    public static boolean isValid(String s) {
        Stack checker = new Stack<Character>();
        HashMap<Character, Character> table = new HashMap<>();
        table.put('(', ')');
        table.put('[', ']');
        table.put('{', '}');
        boolean flag = true;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (checker.isEmpty()) {
                checker.push(c);
            } else if (table.containsKey(c)) {
                checker.push(c);
            } else {
                try {
                    if (table.get(checker.peek()) == c) {
                        checker.pop();
                    } else {
                        flag = false;
                    }
                } catch (Exception e) {
                    flag = false;
                }
            }
        }
        if (!checker.isEmpty()) {
            flag = false;
        }
        return flag;

    }
}
