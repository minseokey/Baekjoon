import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        
        ArrayList<Integer> tmp = new ArrayList<>();
        for(int i : people){
            tmp.add(i);
        }
        tmp.sort((o1,o2) -> {return o1 - o2;});
        
        Deque<Integer> lis = new ArrayDeque<>();
        for(int i : tmp){
            lis.add(i);
        }
        
        int ans = 0;
        
        while(lis.size() > 0){
            int capa = limit - lis.removeFirst();
            while(lis.size() > 0){
                int now = lis.removeLast();
                if(capa >= now){
                    break;
                }
                else{
                    ans ++;
                }
            }
            ans ++;
        }
        return ans;
    }
}