import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true){
            int now = Integer.parseInt(br.readLine());
            if (now == 0){
                break;
            }
            char[] newNow = String.valueOf(now).toCharArray();
            boolean key = false;
            for(int i = 0; i < newNow.length/2; i++){
                if(newNow[i] != newNow[newNow.length - (i + 1)]){
                    bw.write("no" + "\n");
                    key = true;
                    break;
                }
            }
            if (!key) {
                bw.write("yes" + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}