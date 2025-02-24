import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static Deque<String> queue = new ArrayDeque<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i ++){
            String[] tmp = br.readLine().split(" ");
            if(tmp[0].equals("push")){
                queue.add(tmp[1]);
            }
            else if(tmp[0].equals("pop")){
                if(queue.isEmpty()){
                    bw.write("-1" + "\n");
                }
                else {
                    bw.write(queue.removeFirst() + "\n");
                }
            }
            else if(tmp[0].equals("size")){
                bw.write(queue.size() + "\n");
            }
            else if(tmp[0].equals("empty")){
                boolean t = queue.isEmpty();
                if(t){
                    bw.write( "1"+ "\n");
                }
                else {
                    bw.write("0" + "\n");
                }
            }
            else if (tmp[0].equals("front")){
                if(queue.isEmpty()){
                    bw.write("-1" + "\n");
                }
                else {
                    bw.write(queue.peekFirst() + "\n");
                }
            }
            else{
                if(queue.isEmpty()){
                    bw.write("-1" + "\n");
                }
                else {
                    bw.write(queue.peekLast() + "\n");
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}