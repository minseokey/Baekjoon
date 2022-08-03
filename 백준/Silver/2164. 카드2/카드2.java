import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		int num = scanner.nextInt();
		int [] arr = new int[num*2];
		for(int i = 1; i <= num; i++){
			arr[i-1] = i;
		}
		for(int i = 0; i < num; i ++){
			if(i % 2 != 0){
				num ++;
				arr[num-1] = arr[i];
				// System.out.println(arr[i]);
			}
			// else{
			// 	System.out.println(arr[i]);
			// }
		}
		System.out.println(arr[num-1]);
		scanner.close();
	}
}