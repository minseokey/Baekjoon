import java.util.*;
import java.io.*;

public class Main{
    static int n;
    static double sum = 0;
    static int max = 0;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        String[] tmp = br.readLine().split(" ");

        for(int i = 0; i < tmp.length; i++){
            sum += Integer.parseInt(tmp[i]);
            max = Math.max(max, Integer.parseInt(tmp[i]));
        }
        bw.write(String.valueOf((sum*100)/(max*tmp.length)));

        bw.flush();
        bw.close();
        br.close();
    }
}