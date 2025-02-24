import java.io.*;
import java.util.*;

public class Main{
    static int n,m;
    static int[] mlis;
    static HashMap<Integer,Integer> nlis = new HashMap<>();
    static ArrayList<List<String>> input = new ArrayList<>();
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        for(Integer i : tmp){
            nlis.put(i, nlis.getOrDefault(i,0) + 1);
        }
        m = Integer.parseInt(br.readLine());
        mlis = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();



        for(int i = 0; i < m; i ++){
            bw.write(String.valueOf(nlis.getOrDefault(mlis[i],0))+ " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}