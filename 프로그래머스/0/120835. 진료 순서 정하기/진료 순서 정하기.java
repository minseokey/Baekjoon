import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] emergency) {
        int[] emergency2 = Arrays.stream(emergency)
            .sorted()
            .toArray();
        
        int[] ans = new int[emergency.length];
        for(int i = 0; i < emergency.length; i++){
            for(int j = 0; j < emergency.length; j++){
                if(emergency[i] == emergency2[j]){
                    ans[i] = emergency.length - j;
                }
            }
        }
        return ans;
        
    }
}

