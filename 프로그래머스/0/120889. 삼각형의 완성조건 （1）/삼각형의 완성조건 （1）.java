import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int maxx = Arrays.stream(sides).max().orElse(0);
        for(int i = 0; i < sides.length; i ++){
            if(sides[i] == maxx){
                sides[i] = 0;
                break;
            }
        }
        if(Arrays.stream(sides).sum() > maxx){
            return 1;
        }
        return 2;
    }
}