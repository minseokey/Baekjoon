import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.HashMap;
import java.io.IOException; 
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;



public class Main {
	public static void main(String[] args)throws IOException {

		BufferedReader scanner = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int onum = Integer.parseInt(scanner.readLine());
		String[] oarr = scanner.readLine().split(" ");
		int dnum = Integer.parseInt(scanner.readLine());
		String[] darr = scanner.readLine().split(" ");

		
		HashMap<String,Integer> hash = new HashMap<String,Integer>();
		for(int i = 0; i < onum; i++){
			if(hash.containsKey(oarr[i])){
				hash.put(oarr[i],hash.get(oarr[i])+1);
			} 
			else{
				hash.put(oarr[i],1);
			}
		}
		for(int i = 0; i < dnum; i ++){
			if(hash.containsKey(darr[i])){
				bw.write((hash.get(darr[i]) +" "));
			}
			else{
				bw.write(0 +" ");
			}
		}
		bw.flush();
		bw.close();
	}
}