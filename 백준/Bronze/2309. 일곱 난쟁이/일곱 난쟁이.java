import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> now = new ArrayList<>();
        int summ = -100;
        for (int i = 0; i < 9; i++) {
            int tmp = Integer.parseInt(br.readLine());
            now.add(tmp);
            summ += tmp;
        }
        boolean key = false;

        for (int i = 0; i <= 9; i++) {
            for (int j = 0; j < i; j++) {
                if (now.get(i) + now.get(j) == summ) {
                    key = true;
                    now.remove(i);
                    now.remove(j);
                    break;
                }
            }
            if (key) {
                break;
            }
        }
        Collections.sort(now);
        for (Integer integer : now) {
            System.out.println(integer);
        }
    }
}
