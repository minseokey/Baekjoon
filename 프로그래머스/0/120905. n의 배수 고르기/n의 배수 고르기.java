import java.util.stream.Collectors;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> answer = new ArrayList<Integer>();
        
        for(int t : numlist){
            if(t % n == 0){
                answer.add(t);
            }
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}