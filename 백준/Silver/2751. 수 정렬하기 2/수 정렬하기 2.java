import java.io.*;
import java.util.*;


public class Main{
    static int n;
    static List<Integer> lis = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i ++){
            lis.add(Integer.parseInt(br.readLine()));
        }
        lis.sort((o1,o2) -> {return o1 - o2;});
        for(Integer i : lis){
            bw.write(String.valueOf(i) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}