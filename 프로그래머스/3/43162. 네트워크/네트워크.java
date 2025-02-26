import java.util.*;

class Solution {
    
    public static int[] uf;
        
    public int solution(int n, int[][] computers) {
        uf = new int[n];
        for(int i = 0; i < n; i++){
            uf[i] = i;
        }
        for(int k = 0; k < 2; k++){
            for(int i = 0; i < n; i ++){
                for(int j = 0; j < n; j ++){
                    if(i != j && computers[i][j] == 1){
                        union(i,j);
                    }
                }
            }
        }
        Set<Integer> ans = new HashSet<>();
        for(Integer i : uf){
            ans.add(i);
        }
        
        return ans.size();
    }
    
    public int find(int a){
        if(uf[a] == a){
            return a;
        }
        uf[a] = find(uf[a]);
        return uf[a];
    } 
    
    public void union(int a, int b){
        a = find(a);
        b = find(b);
        
        if(a > b){
            uf[a] = b;
        }
        else if(b > a){
            uf[b] = a;
        }
    }
        
}