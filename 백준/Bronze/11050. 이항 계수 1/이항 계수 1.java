import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException; 
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;



public class Main {
	public static void main(String[] args)throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String[] inp = br.readLine().split(" ");
		int big = Integer.parseInt(inp[0]);
		int sma = Integer.parseInt(inp[1]);
		int bigg = 1;
		int smaa = 1;
		while(sma != 0){
			bigg *= big;
			big--;
			smaa *= sma;
			sma--;
		}
		
		System.out.print(bigg/smaa);

		bw.flush();
		bw.close();
	}
}