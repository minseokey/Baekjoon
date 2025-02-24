import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static HashMap<Integer, ArrayList<List<Integer>>> map = new HashMap<>();
    static int checksum;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        for(int i = 1; i <= n; i ++){
            String[] tmp = br.readLine().split(" ");
            int t = Integer.parseInt(tmp[0]);
            ArrayList<List<Integer>> tmp2 = new ArrayList<>();
            for(int j = 1; j < tmp.length -1; j+=2){
                tmp2.add(List.of(Integer.parseInt(tmp[j]), Integer.parseInt(tmp[j+1])));
            }
            map.put(t,tmp2);
        }

        // 1 기준 가장 먼 지점 탐색.
        PriorityQueue<List<Integer>> queue = new PriorityQueue<>((o1,o2) -> {return o1.get(0) - o2.get(0);});
        int[] dist = new int[n+1];
        for(int i = 0; i <= n; i ++){
            dist[i] = Integer.MAX_VALUE;
        }
        dist[1] = 0;
        queue.add(List.of(0,1)); // value, node

        while(!queue.isEmpty()){
            List<Integer> tmp = queue.poll();
            int now = tmp.get(1);
            for(List<Integer> nex: map.get(now)){
                if(dist[nex.get(0)] > dist[now] + nex.get(1)){
                    dist[nex.get(0)] = dist[now] + nex.get(1);
                    queue.add(List.of(dist[nex.get(0)], nex.get(0)));
                }
            }
        }
        int tmp = 0;
        for(int i = 1; i <= n; i ++){
            if(tmp < dist[i]){
                checksum = i;
                tmp = dist[i];
            }
        }
        // 가장 먼 지점 기준 가장 먼 지점 탐색.
        PriorityQueue<List<Integer>> queue2 = new PriorityQueue<>((o1,o2) -> {return o1.get(0) - o2.get(0);});
        int[] dist2 = new int[n+1];
        for(int i = 0; i <= n; i++){
            dist2[i] = Integer.MAX_VALUE;
        }
        dist2[checksum] = 0;
        queue2.add(List.of(0,checksum));

        while (!queue2.isEmpty()){
            int now = queue2.poll().get(1);
            for(List<Integer> nex : map.get(now)){
                if(dist2[nex.get(0)] > dist2[now] + nex.get(1)){
                    dist2[nex.get(0)] = dist2[now] + nex.get(1);
                    queue2.add(List.of(dist[nex.get(0)], nex.get(0)));
                }
            }
        }

        int tmp2 = 0;
        for(int i = 1; i <= n; i ++){
            if(tmp2 < dist2[i]){
                tmp2 = dist2[i];
            }
        }
        bw.write(String.valueOf(tmp2));

        bw.flush();
        bw.close();
        br.close();
    }
}