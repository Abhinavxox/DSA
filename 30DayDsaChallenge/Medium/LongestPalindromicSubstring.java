package Medium;

public class LongestPalindromicSubstring {
    public String longestPalindrome(String s) {
        StringBuilder reverse = new StringBuilder();
        for(int i=s.length(); i>0; i--){
            reverse.append(s.charAt(i));
        }
        
    }
}
