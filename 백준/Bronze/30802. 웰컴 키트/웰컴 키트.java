import java.io.*;
import java.util.*;

public class Main{
    static int n, t, p;
    static int sum = 0;
    static int sum2 = 0;

    static int[] cnt = new int[6];


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        String[] tmp = br.readLine().split(" ");
        for(int i = 0; i < 6; i ++){
            cnt[i] = Integer.parseInt(tmp[i]);
            sum += cnt[i];
        }
        String[] tmp2 = br.readLine().split(" ");
        t = Integer.parseInt(tmp2[0]);
        p = Integer.parseInt(tmp2[1]);

        for(int i = 0; i < 6; i ++){
            sum2 += Math.ceil((double)cnt[i]/t);
        }
        bw.write(sum2+"\n");
        bw.write((sum/p) + " " + (sum%p));
        bw.flush();
        bw.close();
        br.close();
    }
}