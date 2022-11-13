import java.util.Scanner;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        
        int a = scanner.nextInt();
        int [] arra = new int [a];
        for(int i = 0; i < a; i++){
            arra[i] = scanner.nextInt();
        }

        int b = scanner.nextInt();
        int [] arrb = new int [b];
        for(int j = 0; j < b; j++){
            arrb[j] = scanner.nextInt();
        }

        Arrays.sort(arra);
        
        for(int i = 0; i < b; i ++){
            int start = 0;
            int end = a;
            while(true){
                int mid = (end+start)/ 2 ;
                if(end == start){
                    System.out.println("0");
                    break;
                }
                else if(arrb[i] == arra[mid]){
                    System.out.println("1");
                    break;
                }
                else if(arrb[i] > arra[mid]){
                    start = mid+1;
                }
                else{
                    end = mid;
                }
            }
        }
        scanner.close();
    }
}

