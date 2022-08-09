package Medium;

import java.util.ArrayList;

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("pwwkew"));
    }

    public static int lengthOfLongestSubstring(String s) {
        int max = 0;
        ArrayList<Character> alist = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (alist.contains(s.charAt(i))) {
                int j = alist.indexOf(s.charAt(i));
                for (int k = 0; k <= j; k++) {
                    alist.remove(0);
                }
            }
            alist.add(s.charAt(i));

            if (alist.size() > max) {
                max = alist.size();
            }
        }
        return max;
    }
}
