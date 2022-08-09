package Medium;

import java.util.ArrayList;

public class LongestSubstringWithoutRepeatingCharacters {
    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("pwwkew"));
    }

    public static int lengthOfLongestSubstring(String s) {
        ArrayList<Character> alist = new ArrayList<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (!alist.contains(c)){
                alist.add(c);
            }
        }
        return alist.size();
    }
}
