import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        // 에라토스테네스의 체 만들기.
        ArrayList<Integer> prime = new ArrayList<>();
        for(int i = 2; i <= n; i ++){
            prime.add(i);
        }

        for(int i = 0; i < prime.size(); i++){
            if(prime.get(i) != 0){
                int now = prime.get(i);
                for (int j = i+now; j < prime.size(); j+=now){
                    prime.set(j,0);
                }
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();

        for(int i = 0; i < prime.size(); i++){
            if(prime.get(i) != 0){
                while(true){
                    if(n%prime.get(i) == 0){
                        ans.add(prime.get(i));
                        n /= prime.get(i);
                    }
                    else {
                        break;
                    }
                }
                if(n == 0){
                    break;
                }
            }
        }
        for(Integer i: ans){
            System.out.println(i);
        }
    }
}
