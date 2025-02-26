import java.util.*;

class Solution {
    static int len;
    
    public int solution(String begin, String target, String[] words) {
        len = begin.length();
        boolean[] visited = new boolean[words.length];
        
        PriorityQueue<List<Integer>> queue = new PriorityQueue<>((o1,o2) -> o1.get(0) - o2.get(0));
        queue.add(List.of(0,0));
        
        while(!queue.isEmpty()){
            List<Integer> tmp = queue.poll();
            String now;
            int cnt = tmp.get(0);
            if(cnt == 0){
                now = begin;
            }
            else{
                now = words[tmp.get(1)];
            }
            
            if(now.equals(target)){
                return cnt;
            }
            for(int i = 0; i < words.length; i ++){
                if(!visited[i]){
                    int diff = 0;
                    String str = words[i];
                    for(int j = 0; j < len; j ++){
                        if(str.charAt(j) != now.charAt(j)){
                            diff+=1;
                        }
                    }
                    if(diff == 1){
                        visited[i] = true;
                        queue.add(List.of(cnt+1, i));
                    }
                }
            }
        }
        return 0;
    }
}