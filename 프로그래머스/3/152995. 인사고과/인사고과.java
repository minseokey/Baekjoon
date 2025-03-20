import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int wansum = scores[0][0] + scores[0][1];
        int wan_a = scores[0][0];
        int wan_b = scores[0][1];
        int rank = 1;
        
        for(int i = 0; i < scores.length; i++){
            if(wan_a < scores[i][0] && wan_b < scores[i][1]){
                return -1;
            }
            else if(scores[i][0] + scores[i][1] > wansum){
                // i가 인센 대상이면 += 1, 아니면 패스.
                for(int j = 0; j < scores.length; j++){
                    if(scores[i][0] < scores[j][0] && scores[i][1] < scores[j][1]){
                        rank -= 1;
                        break;
                    }
                }
                rank += 1;
            }
        }
        return rank;
    }
}