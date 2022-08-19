package Medium;

public class LongestPanlindromicSubstring {

    public static void main(String[] args) {
        System.out.println(longestPalindrome("abb"));
        ;
    }

    public static String longestPalindrome(String s) {
        if (s.length() == 1) {
            return s;
        }
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        String s2 = sb.toString();

        // find the longest common palindrome between s and s2
        String palindrome = "";
        StringBuilder temp = new StringBuilder();
        for (int i = 0; i < s.length() - 1; i++) {
            for (int j = i; j < s.length(); j++) {
                if (s.charAt(j) == s2.charAt(j)) {
                    temp.append(s.charAt(j));
                } else {
                    if (temp.toString().length() > palindrome.length()) {
                        palindrome = temp.toString();
                    }
                    temp.setLength(0);
                }
            }
            if (palindrome.isEmpty()) {
                palindrome = temp.toString();
            }
        }

        return palindrome;
    }

}
