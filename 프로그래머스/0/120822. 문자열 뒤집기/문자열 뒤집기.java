import java.util.*;

class Solution {
    public String solution(String my_string) {
        char[] newChar = new char[my_string.length()];
        for (int i= 0; i < my_string.length(); i ++){
            newChar[i] = my_string.charAt(my_string.length() - i - 1);
        }
        return String.valueOf(newChar);
    }
}