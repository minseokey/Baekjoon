import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static HashSet<String> all = new HashSet<>();


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++){
            all.add(br.readLine().strip());
        }
        ArrayList<String> newall = new ArrayList<>(all);
        newall.sort((o1, o2) -> {
            if (o1.length() == o2.length()) {
                return o1.compareTo(o2);
            }
            return o1.length() - o2.length();
        });

        for(String i : newall){
            bw.write(i+"\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}