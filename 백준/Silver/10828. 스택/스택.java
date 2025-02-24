import java.io.*;
import java.util.*;

public class Main{
    static int n;
    static Stack<String> stack = new Stack<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i ++){
            String[] tmp = br.readLine().split(" ");
            if(tmp[0].equals("push")){
                stack.add(tmp[1]);
            }
            else if(tmp[0].equals("pop")){
                if(stack.isEmpty()){
                    bw.write("-1" + "\n");
                }
                else {
                    bw.write(stack.pop() + "\n");
                }
            }
            else if(tmp[0].equals("size")){
                bw.write(stack.size() + "\n");
            }
            else if(tmp[0].equals("empty")){
                boolean t = stack.isEmpty();
                if(t){
                    bw.write( "1"+ "\n");
                }
                else {
                    bw.write("0" + "\n");
                }
            }
            else{
                if(stack.isEmpty()){
                    bw.write("-1" + "\n");
                }
                else {
                    bw.write(stack.peek() + "\n");
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}