import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String cipher, int code) {
        StringBuilder tmp = new StringBuilder();
        
        for(int i = code-1; i < cipher.length(); i += code){
            tmp.append(cipher.charAt(i));
        }
        return tmp.toString();
    }
}