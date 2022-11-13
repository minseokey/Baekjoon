
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

class stack{
    int[] arr;
    int top;

    void init(int t){
        this.top = -1;
        this.arr = new int[t];
    }
    void push(int value){
        top++;
        arr[top] = value;
    }
    int pop(){
        if(top == -1){
            return -1;
        }
        else{
            int temp = arr[top];
            top --;
            return temp;
        }
    }
    int size(){
        return top + 1;
    }
    int empty(){
        if(top == -1){
            return 1;
        }
        else{
            return 0;
        }
    }
    int top() {
        if (top == -1) {
            return -1;
        }
        else {
            return arr[top];
        }
    }

}



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for (int i = 0; i < n; i++) {
            stack a = new stack();
            String input = bf.readLine();
            a.init(input.length());
            boolean ch = true;
            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == '(') {
                    a.push('(');
                }
                else{
                    if(a.pop() == -1){
                        System.out.println("NO");
                        ch = false;
                        break;
                    }
                }
            }
            if(ch && a.top == -1){
                System.out.println("YES");
            }
            else if(ch){
                System.out.println("NO");
            }
        }
    }
}

