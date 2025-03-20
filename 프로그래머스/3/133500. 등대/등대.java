import java.util.*;

class Solution {
    static Map<Integer, List<Integer>> map = new HashMap<>();
    static int ans = 0;
    static boolean[] light;
    public int solution(int n, int[][] lighthouse) {
        for(int i = 0; i < lighthouse.length; i ++){
            if(!map.containsKey(lighthouse[i][0])){
                map.put(lighthouse[i][0], new ArrayList<>());
            }
            map.get(lighthouse[i][0]).add(lighthouse[i][1]);
            
            if(!map.containsKey(lighthouse[i][1])){
                map.put(lighthouse[i][1], new ArrayList<>());
            }
            map.get(lighthouse[i][1]).add(lighthouse[i][0]);
        }
        
        
        light = new boolean[n+1];
        for(int i = 0; i <= n; i++){
            light[i] = false;
        }
        
        dfs(1,1); // 1번에서 시작. 1이 리프다.
        
        return ans;
    }
    
    //리프까지 내려간다. 리프는 절대 켜지면 안됨. 
    private void dfs(int node, int parent){
        for(int child : map.get(node)){
            if(child != parent){
                dfs(child, node);
                if(!light[child] && !light[node]){
                    light[node] = true;
                    ans += 1;
                }
            }
        }
    }
}