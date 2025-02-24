import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            List<Integer> tmp = new ArrayList<>();
            tmp.add(Integer.parseInt(st.nextToken()));
            tmp.add(Integer.parseInt(st.nextToken()));
            tmp.add(Integer.parseInt(st.nextToken()));
            if (tmp.get(0) == 0){
                break;
            }
            tmp.sort((o1,o2) -> {return o1-o2;});

            if(Math.pow(tmp.get(2),2) == Math.pow(tmp.get(0),2)+ Math.pow(tmp.get(1),2)){
                bw.write("right" + "\n");
            }
            else{
                bw.write("wrong" + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}