import java.io.*;
import java.util.*;


public class Main{
    static int n;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        n = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();
        for(int i = 1; i <= n; i++){
            deque.add(i);
        }

        while (deque.size() > 1){
            deque.removeFirst();
            deque.addLast(deque.removeFirst());
        }

        bw.write(String.valueOf(deque.getFirst()));
        bw.flush();
        bw.close();
        br.close();
    }
}