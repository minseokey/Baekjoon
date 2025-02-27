import java.util.*;


class Solution {
    
    static Map<Integer, List<Integer>> field = new HashMap<>();
    
    public int solution(int n, int[][] edge) {
        int ans = 0;
        for(int i = 1; i <= n; i ++){
            field.put(i, new ArrayList<>());
        }
        for(int i = 0; i < edge.length; i++){
            field.get(edge[i][0]).add(edge[i][1]);
            field.get(edge[i][1]).add(edge[i][0]);
        }
        
        PriorityQueue<List<Integer>> queue = new PriorityQueue<>((o1,o2) -> {return o1.get(0) - o2.get(0);});
        queue.add(List.of(0,1)); // wei 0, node 1;
        
        int[] visited = new int[n+1];
        for(int i = 0; i <= n; i++){
            visited[i] = 0;
        }
        visited[1] = -1;
        
        while(!queue.isEmpty()){
            List<Integer> tmp = queue.poll();
            int node = tmp.get(1);
            int cnt = tmp.get(0);

            for(int i : field.get(node)){
                if(visited[i] == 0){ // 방문하지 않았을때;
                    visited[i] = cnt+1;
                    queue.add(List.of(cnt+1, i));
                }
            }
        }
        int max = Integer.MIN_VALUE;
        
        for(int i : visited){
            max = Math.max(i, max);
        }
        for(int i : visited){
            if(max == i){
                ans += 1;
            }
        }
        
        return ans;
    }
}