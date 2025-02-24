import java.io.*;
import java.util.*;

public class Main{

    static int a,b,c;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] tmp = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        a = tmp[0];
        b = tmp[1];
        c = tmp[2];

        bw.write(String.valueOf(recur(b) % c));
        bw.flush();
        bw.close();
        br.close();
    }

    public static long recur(int mul){
        if(mul <= 0){
            return 1;
        }
        else{
            if(mul%2 == 1){
                long n = recur(mul/2);
                return (((n*n) % c) * a) % c;
            }
            else{
                long n = recur(mul/2);
                return (n*n) % c;
            }
        }
    }
}