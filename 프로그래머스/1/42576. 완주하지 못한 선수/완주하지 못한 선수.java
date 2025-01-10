import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String,Integer> tmp = new HashMap<String,Integer>();
        String ans = "";
        for(String comp: completion){
            if(tmp.keySet().contains(comp)){
                tmp.replace(comp, tmp.get(comp)+1);
            }
            else{
                tmp.put(comp,1);
            }
        }
        Set<String> keyset = tmp.keySet();
        
        for(String part: participant){
            if(keyset.contains(part) && tmp.get(part) > 0){
                tmp.replace(part,tmp.get(part)-1);
            }
            else{
                ans = part;
            }
        }
        return ans;
    }
}