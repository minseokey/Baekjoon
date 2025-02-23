import java.io.*;
import java.util.*;

public class Main{
    static int y,x;
    static char[][] field;
    static int cnt = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        y = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        field = new char[y][x];

        for(int i = 0; i < y; i++){
            // 연속된 문자열을 한글자씩 Char로 분리.
            field[i] = br.readLine().toCharArray();
        }

        for(int ty = 0; ty <= y-8; ty++){
            for(int tx = 0; tx <= x-8; tx++){
                cnt = Math.min(rewrite(ty,tx), cnt);
            }
        }

        bw.write(String.valueOf(cnt));
        bw.flush();
        br.close();
        bw.close();
    }

    private static int rewrite(int sy, int sx){
        boolean key = field[sy][sx] == 'B';
        int cnt1 = 0;
        int cnt2 = 0;
        for(int ny = sy; ny < sy+8; ny++){
            for(int nx = sx; nx < sx+8; nx++){
                if((field[ny][nx] == 'B' && !key) || (field[ny][nx] == 'W' && key) ){
                    cnt1++;
                }
                else{
                    cnt2++;
                }
                key = !key;
            }
            key = !key;
        }
        return Math.min(cnt1, cnt2);
    }
}