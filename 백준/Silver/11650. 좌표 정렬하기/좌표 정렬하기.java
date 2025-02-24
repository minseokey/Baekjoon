import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main{
    static int a;
    static ArrayList<int[]> lis = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        a = Integer.parseInt(br.readLine());
        for(int i = 0; i < a; i ++){
            lis.add(
                    Arrays.stream(
                            br.readLine().split(" ")
                    ).mapToInt(Integer::parseInt).toArray()
            );
        }

        lis.sort((o1,o2) -> {
            if (o1[0] == o2[0]){
                return o1[1] - o2[1];
            }
            else{
                return o1[0] - o2[0];
            }
        });

        for(int[] t : lis){
            bw.write(t[0] + " " + t[1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}