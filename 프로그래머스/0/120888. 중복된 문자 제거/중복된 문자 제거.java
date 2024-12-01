import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String my_string) {
        return my_string.chars()
            .distinct()
            .mapToObj(t -> String.valueOf((char)t))
            .collect(Collectors.joining());
    }
}