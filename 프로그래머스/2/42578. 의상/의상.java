import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String,Integer> tmp = new HashMap<>();

        for(String[] cloth: clothes){
            if(tmp.keySet().contains(cloth[1])){
                tmp.replace(cloth[1],tmp.get(cloth[1]) + 1);
            }
            else{
                tmp.put(cloth[1],1);
            }
        }
        int ans = 1; // 곱셈을 위한 초기값 설정
        
        // 각 종류별 의상 선택 경우의 수 계산
        for (int count : tmp.values()) {
            ans *= (count + 1); // 해당 의상 종류를 선택하지 않는 경우를 포함
        }
        
        return ans - 1; // 모든 종류에서 선택하지 않는 경우(공집합) 제외
    }
}