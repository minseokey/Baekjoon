import java.util.*;

class Solution {
    
    public int solution(int n, int[][] results) {
        int[][] field = new int[n+1][n+1];
        for(int i = 0; i < results.length; i++){
            field[results[i][0]][results[i][1]] = 1;
            field[results[i][1]][results[i][0]] = -1;
        }
        for(int k = 1; k <= n; k++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                   if(k!=i && k!=j && j!=i){
                       if(field[i][k] == 1 && field[k][j] == 1 && field[i][j] == 0){
                           field[i][j] = 1;
                       }
                       else if(field[i][k] == -1 && field[k][j] == -1 && field[i][j] == 0){
                           field[i][j] = -1;
                       }
                   }
                }
            }
        }
        int ans = 0;
        for(int i = 1; i <= n; i++){
            boolean tmp = false;
            for(int j = 1; j <= n; j++){
                if(i != j && (field[i][j] == 0 || field[j][i] == 0)){
                    tmp = true;
                    break;
                }
            }
            if(!tmp){
                ans ++;
            }
        }
        
    return ans;
    }
}