import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;


class deque{
	int front;
	int back;
	int[] arr;
	static final int MAX = 100000;
	
	void init() {
		arr = new int[MAX];
		front = 0;
		back = 0;
		}
	void push_front(int value) {
		front --;
		arr[(MAX+front) % MAX] = value;
	}
	void push_back(int value) {
		arr[(MAX+back)%MAX] = value;
		back++;
	}
	int pop_front() {
		if(back <= front) {
			return -1;
		}
		else{
			int temp = arr[(MAX + front) % MAX];
			front ++;
			return temp;
		}
	}
	int pop_back() {
		if(back <= front) {
			return -1;
		}
		else {
			back--;
			return arr[(MAX+back)% MAX];
		}
	}
	int size() {
		return back - front;
	}
	int empty() {
		if(front == back) {
			return 1;
		}
		else {
			return 0;
		}
	}
	int front() {
		if(front == back) {
			return -1;
		}
		else {
			return arr[(MAX + front) % MAX];
		}
	}
	int back() {
		if(front == back) {
			return -1;
		}
		else {
			return arr[(MAX + back-1) % MAX];
		}
		
	}
	void printdeque() {
		for(int i = 0; i < this.size(); i ++) {
			System.out.print(arr[(MAX+front + i) % MAX] + "  ");
		}
		System.out.println("\n");
	}
	
}


public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		deque a = new deque();
		a.init();
		for(int i = 0; i < n; i ++) {
			String[] inarr = br.readLine().split(" ");
			switch(inarr[0]) {
			case "push_front":
				a.push_front(Integer.parseInt(inarr[1]));
				break;
			case "push_back":
				a.push_back(Integer.parseInt(inarr[1]));
				break;
			case "pop_front":
				bw.write(a.pop_front()+"\n");
				break;
			case "pop_back":
				bw.write(a.pop_back()+"\n");
				break;
			case "size":
				bw.write(a.size()+"\n");
				break;
			case "empty":
				bw.write(a.empty()+"\n");
				break;
			case "front":
				bw.write(a.front()+"\n");
				break;
			case "back":
				bw.write(a.back()+"\n");
			}
		}
		bw.close();
	}
}
