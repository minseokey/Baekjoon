import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Comparator;

class Solution {
    public int solution(int[] array) {
        List<Integer> tmp = 
            Arrays.stream(array).boxed().collect(Collectors.toList());
        tmp.sort(Comparator.comparing(t -> t));
        System.out.println(tmp);
        return tmp.get((int)array.length/2);
    }
}