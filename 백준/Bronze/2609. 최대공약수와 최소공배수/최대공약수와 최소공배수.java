import java.util.Scanner;

public class Main {
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		int numa = scanner.nextInt();
		int numb = scanner.nextInt();
		int maxx = numa * numb;
		if(numa < numb){
			int temp = numb;
			numb = numa;
			numa = temp;
		}

		while(numa % numb != 0){
			int temp = numb;
			numb = numa%numb;
			numa = temp;
		}
		int max = numb;
		int min = maxx/max;

		System.out.println(max);
		System.out.println(min);

		scanner.close();
	}
}