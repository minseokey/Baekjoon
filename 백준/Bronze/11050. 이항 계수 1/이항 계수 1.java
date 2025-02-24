import java.io.*;
import java.util.*;

public class Main{
    static int a,b;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] tmp = br.readLine().split(" ");
        a = Integer.parseInt(tmp[0]);
        b = Integer.parseInt(tmp[1]);
        b = Math.min(b, a-b);

        int top = 1;
        int bot = 1;

        for(int i = 1; i <= b; i++){
            bot *= i;
            top *= a+1-i;
        }
        bw.write(String.valueOf(top/bot));
        bw.flush();
        bw.close();
        br.close();
    }
}