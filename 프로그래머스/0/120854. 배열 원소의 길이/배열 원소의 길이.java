import java.util.*;
import static java.util.stream.Collectors.*;

class Solution {
    public int[] solution(String[] strlist) {
        return Arrays.stream(strlist).mapToInt(String::length).toArray();
    }
}