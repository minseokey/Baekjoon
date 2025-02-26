import java.util.*;

class Solution {
    public int solution(int[] citations) {
        ArrayList<Integer> cita = new ArrayList<>();
        for(int i : citations){
            cita.add(i);
        }
        cita.sort((o1,o2) -> {return o2 - o1;});
        
        for(int i = 0; i < citations.length; i++){
            if(cita.get(i) <= i){
                return i;
            }
        }
        return cita.size();
    }
}