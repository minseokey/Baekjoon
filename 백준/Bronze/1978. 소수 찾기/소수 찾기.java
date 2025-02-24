import java.io.*;
import java.util.*;


public class Main{

    static int n, max_val;
    static int[] lis;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        lis = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] prime = new int[1001];
        for(int i = 0; i < 1001; i ++ ){
            prime[i] = i;
        }
        prime[0] = 0;
        prime[1] = 0;

        for(int i = 0; i < 1001; i++){
            if(prime[i] != 0){
                for(int j = i*2; j<1001; j+= i){
                    prime[j] = 0;
                }
            }
        }
        int ans = 0;

        for(Integer i : lis){
            if(prime[i] != 0){
                ans++;
            }
        }
        bw.write(String.valueOf(ans));
        bw.flush();
        bw.close();
        br.close();
    }
}