import java.util.*;

class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int ww = 2*w;
        
        answer += Math.ceil((double)(stations[0] - w - 1) / (ww+1));
        for(int i = 1; i < stations.length; i++){
            answer += Math.ceil((double)(stations[i] - stations[i-1] - ww - 1) / (ww+1));
        }
        if(n - stations[stations.length - 1] - w > 0){
            answer += Math.ceil((double)(n - stations[stations.length - 1] - w) / (ww+1));
        }
        
    
        return answer;
    }
}