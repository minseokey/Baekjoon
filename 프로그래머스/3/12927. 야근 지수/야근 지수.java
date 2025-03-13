import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> tmp = new PriorityQueue<>(Collections.reverseOrder());
        long ans = 0;
        for(int i : works){
            tmp.add(i);
        }
        
        for(int i = 0; i < n; i ++){
            int tt = tmp.poll();
            if (tt > 0){
                tmp.add(tt - 1);
            }
            else{
                tmp.add(tt);
                break;
            }
        }
        while(!tmp.isEmpty()){
            ans += Math.pow(tmp.poll(),2);
        }
        
        return ans;
    }
}