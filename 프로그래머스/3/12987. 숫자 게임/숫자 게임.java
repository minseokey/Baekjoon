import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        List<Integer> BB = new ArrayList<>();
        for(int i : B){
            BB.add(i);
        }
        BB.sort((o1,o2) -> {return o1 - o2;});
        
        List<Integer> AA = new ArrayList<>();
        for(int i : A){
            AA.add(i);
        }
        AA.sort((o1,o2) -> {return o1 - o2;});
        
        
        int a = 0;
        int b = 0;
        int ans = 0;
        
        while(b < B.length){
            if(AA.get(a) < BB.get(b)){
                a += 1;
                b += 1;
                ans += 1;
            }
            else{
                b += 1;
            }
        }
        
        return ans;
    }
}