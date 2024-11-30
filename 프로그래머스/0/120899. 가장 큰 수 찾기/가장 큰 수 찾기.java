import java.util.Arrays;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] array) {
        int max = Arrays.stream(array).max().orElse(0);
        int ind = IntStream.range(0,array.length).filter(n -> array[n]==max).findFirst().orElse(-1);
        int[] ans = {max, ind};
        return ans;
    }
}