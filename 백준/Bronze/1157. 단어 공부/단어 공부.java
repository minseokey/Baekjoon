
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String Wor = scanner.nextLine();
		char[] Worlis = Wor.toCharArray();
		int count = 0;
		for(char a : Worlis) {
			
			if(Character.isLowerCase(a)){
				Worlis[count] = Character.toUpperCase(a);
			}
			count = count + 1;
		}
		String alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		char[]alplis = alp.toCharArray();
		int[] numlis = new int[26];
		for(int i = 0; i <alplis.length;i++) {
			for(char j : Worlis){
				if(alplis[i] == j) {
					numlis[i] = numlis[i] + 1;
				}
				
			}
		}
		int max = 0;
		int foi = 0;
		int coun = 0;
		int maxcoun = 0;
		for(int i : numlis) {
			if(i > max) {
				max = i;
				maxcoun = coun;
			}
			coun = coun + 1;
		}
		for (int i: numlis) {
			if(max == i) {
				foi = foi + 1;
			}
		}
		if(foi >= 2) {
			System.out.println("?");
		}
		else {
			System.out.println(alplis[maxcoun]);
		}
			
		}
	}