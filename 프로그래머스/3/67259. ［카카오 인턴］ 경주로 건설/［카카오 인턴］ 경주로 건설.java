import java.util.*;

class Solution {
    
    static int[] dy = {0,-1,0,1};
    static int[] dx = {1,0,-1,0};
    
    public int solution(int[][] board) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((o1,o2) -> {return o1[0] - o2[0];});
        queue.add(new int[]{0,0,0,0});
        queue.add(new int[]{0,0,0,3});
        int[][][] cost = new int[board.length][board[0].length][4];
        for(int i = 0; i < board.length; i ++){
            for(int j = 0; j < board[i].length; j++){
                for(int k = 0; k < 4; k++){
                    cost[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }
        cost[0][0][0] = 0;
        cost[0][0][3] = 0;
        
        while(!queue.isEmpty()){
            int[] tt = queue.poll();
            int w = tt[0];
            int y = tt[1];
            int x = tt[2];
            int d = tt[3];
            
            if(y == board.length - 1 && x == board[0].length - 1){
                return w;
            }
            for(int i = 0; i < 4; i ++){
                if(x + dx[i] < board[0].length && y + dy[i] < board.length && y + dy[i] >= 0 && x + dx[i] >= 0 && board[dy[i] + y][dx[i] + x] == 0){
                    // 같은방향
                    if(i == d && cost[y+dy[i]][x+dx[i]][i] > w+100){
                        queue.add(new int[]{w+100, y + dy[i],x + dx[i],i});
                        cost[y+dy[i]][x+dx[i]][i] = w+100;
                    }
                    else if ((i+d) % 2 == 1 && cost[y+dy[i]][x+dx[i]][i] > w+600){
                        queue.add(new int[]{w+600, y + dy[i],x + dx[i],i});
                        cost[y+dy[i]][x+dx[i]][i] = w+600;
                    }
                }
            }
            
        }
        return 0;
    }
}