
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

class queue{
    int front;
    int back;
    int[] arr;

    void init(int t){
        arr = new int[t];
        front = -1;
        back = -1;
    }
    void push(int value){
        back++;
        arr[back] = value;
    }
    int pop(){
        if(back - front != 0){
        front ++;
        return arr[front];
        }
        else{
            return -1;
        }
    }
    int size(){
        return back - front;
    }
    int empty(){
        if(back - front == 0){
            return 1;
        }
        else{
            return 0;
        }
    }
    int front(){
        if(back - front != 0) {
            return arr[front + 1];
        }
        else{
            return -1;
        }
    }
    int back(){
        if(back - front != 0) {
            return arr[back];
        }
        else{
            return -1;
        }
    }

}



public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        queue a = new queue();
        int n = Integer.parseInt(bf.readLine());
        a.init(1000000);
        for (int i = 0; i < n; i++) {
            String[] input = bf.readLine().split(" ");
            switch (input[0]) {
                case "push":
                    a.push(Integer.parseInt(input[1]));
                    break;
                case "pop":
                    System.out.println(a.pop());
                    break;
                case "size":
                    System.out.println(a.size());
                    break;
                case "empty":
                    System.out.println(a.empty());
                    break;
                case "front":
                    System.out.println(a.front());
                    break;
                case "back":
                    System.out.println(a.back());
            }
        }
    }
}
