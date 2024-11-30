import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<Integer>();
        for(int i = 0; i <= n; i ++){
            if(i%2 == 1){
                answer.add(i);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}