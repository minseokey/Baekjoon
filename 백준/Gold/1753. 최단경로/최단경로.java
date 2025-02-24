import java.io.*;
import java.util.*;

public class Main {

    static int v, e;
    static int start;
    static HashMap<Integer, List<List<Integer>>> map = new HashMap<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] tmp1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        v = tmp1[0];
        e = tmp1[1];
        start = Integer.parseInt(br.readLine());

        for (int i = 1; i <= v; i++) {
            map.put(i, new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            map.get(tmp[0]).add(List.of(tmp[1], tmp[2]));
        }
        PriorityQueue<List<Integer>> queue = new PriorityQueue<>((o1, o2) -> o1.get(0) - o2.get(0));
        queue.add(List.of(0, start));

        int[] dist = new int[v+1];
        for (int i = 1; i <= v; i++) {
            dist[i] = Integer.MAX_VALUE;
        }
        dist[start] = 0;
        while (!queue.isEmpty()) {
            int now = queue.poll().get(1);
            for (List<Integer> nex : map.get(now)) {
                if (dist[nex.get(0)] > dist[now] + nex.get(1)) {
                    dist[nex.get(0)] = dist[now] + nex.get(1);
                    queue.add(List.of(dist[nex.get(0)], nex.get(0)));
                }
            }
        }
        for(int i = 1; i <= v; i ++){
            if(dist[i] == Integer.MAX_VALUE){
                bw.write("INF" + "\n");
            }
            else {
                bw.write(dist[i] + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}