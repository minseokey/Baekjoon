import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static ArrayList<int[]> field = new ArrayList<>();


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i ++){
            field.add(Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        }

        for(int i = 1; i < n; i ++){
            field.get(i)[0] += Math.min(field.get(i-1)[1], field.get(i-1)[2]);
            field.get(i)[1] += Math.min(field.get(i-1)[0], field.get(i-1)[2]);
            field.get(i)[2] += Math.min(field.get(i-1)[0], field.get(i-1)[1]);
        }

        bw.write(String.valueOf(Math.min(Math.min(field.get(n-1)[0], field.get(n-1)[1]), field.get(n-1)[2])));
        bw.flush();
        bw.close();
        br.close();
    }
}