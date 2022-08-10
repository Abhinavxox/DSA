package Easy;

public class LongestCommonPrefix {
    public static void main(String[] args) {
        String[] str = { "ab", "a" };
        System.out.println(longestCommonPrefix(str));
    }

    public static String longestCommonPrefix(String[] strs) {
        StringBuilder prefix = new StringBuilder();
        boolean flag = true;
        for (int i = 0; i < strs[0].length(); i++) {
            if (!flag)
                break;
            char c = strs[0].charAt(i);
            try {
                for (String x : strs) {
                    if (x.charAt(i) != c) {
                        flag = false;
                    }
                }
                if (flag)
                    prefix.append(c);
            } catch (Exception e) {
                flag = false;
            }
        }
        return prefix.toString();
    }
}
