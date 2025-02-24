import java.io.*;
import java.util.*;

public class Main {

    static int fois;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        fois = Integer.parseInt(br.readLine());
        for(int i = 0; i < fois; i ++){
            ArrayList<List<Integer>> lis = new ArrayList<>();
            int n,m,w;
            int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            n = tmp[0];
            m = tmp[1];
            w = tmp[2];
            for(int j = 0; j < m; j++){
                int[] tmp1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                lis.add(List.of(tmp1[0],tmp1[1],tmp1[2]));
                lis.add(List.of(tmp1[1],tmp1[0],tmp1[2]));
            }
            for(int j = 0; j < w; j++){
                int[] tmp1 = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                lis.add(List.of(tmp1[0],tmp1[1],-tmp1[2]));
            }
            int[] dist = new int[n+1];
            for(int j = 1; j <= n; j ++){
                dist[j] = 10001;
            }
            dist[1] = 0;
            boolean key = true;
            for(int j = 1; j <= n; j++){
                for(int l = 0; l < lis.size(); l++){
                    int now = lis.get(l).get(0);
                    int nex = lis.get(l).get(1);
                    int wei = lis.get(l).get(2);
                    if(dist[nex] > dist[now] + wei){
                        dist[nex] = dist[now] + wei;
                        if(j == n){
                            key = false;
                        }
                    }
                }
            }
            if(key){
                bw.write("NO" + "\n");
            }
            else{
                bw.write("YES" + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}