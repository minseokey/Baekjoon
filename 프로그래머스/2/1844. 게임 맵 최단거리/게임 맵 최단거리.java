import java.util.*;

class Solution {
    static int[] dy = {0,0,-1,1};
    static int[] dx = {-1,1,0,0};
    static int len_y, len_x;
    
    public int solution(int[][] maps) {
        int answer = Integer.MAX_VALUE;
        len_y = maps.length;
        len_x = maps[0].length;
        
        boolean[][] visited = new boolean[len_y][len_x];
        PriorityQueue<List<Integer>> queue = new PriorityQueue<>((o1,o2) -> o1.get(0) - o2.get(0));
        queue.add(List.of(1,0,0)); // wei, y, x
        visited[0][0] = true;
        
        while(!queue.isEmpty()){
            List<Integer> tmp = queue.poll();
            int wei = tmp.get(0);
            int y = tmp.get(1);
            int x = tmp.get(2);
            if(y == len_y-1 && x== len_x-1){
                answer = Math.min(answer, wei);
            }
            
            for(int i = 0; i < 4; i ++){
                if((0 <= y+dy[i]) && (y+dy[i] < len_y) && (0 <= x+dx[i]) && (x+dx[i] < len_x) && maps[y+dy[i]][x+dx[i]] == 1 && !visited[y+dy[i]][x+dx[i]]){
                    visited[y+dy[i]][x+dx[i]] = true;
                    queue.add(List.of(wei+1, y+dy[i], x+dx[i]));
                }
            }
        }
        if(answer == Integer.MAX_VALUE){
            return -1;
        }
        return answer;
    }
}