package Easy;

public class ImplementString {

    public static void main(String[] args) {
        System.out.println(strStr("aaa", "aaaa"));
        ;
    }

    public static int strStr(String haystack, String needle) {
        if (needle.isEmpty()) {
            return 0;
        }
        boolean flag = false;
        for (int i = 0; i < haystack.length(); i++) {
            char c = haystack.charAt(i);
            if (c == needle.charAt(0)) {
                for (int j = 0; j < needle.length(); j++) {
                    try {
                        if (haystack.charAt(i + j) != needle.charAt(j)) {
                            flag = false;
                            break;
                        } else {
                            flag = true;
                        }
                    } catch (Exception e) {
                        return -1;
                    }
                }
                if (flag) {
                    return i;
                }
            }

        }
        return -1;
    }
}
