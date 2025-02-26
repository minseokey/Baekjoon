import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        int count = 0; // 제거한 개수
        
        for (char digit : number.toCharArray()) {
            while (!stack.isEmpty() && count < k && stack.peekLast() < digit) {
                stack.pollLast(); 
                count++;
            }
            stack.addLast(digit);
        }
        
        StringBuilder result = new StringBuilder();
        int size = number.length() - k;
        for (int i = 0; i < size; i++) {
            result.append(stack.pollFirst());
        }
        
        return result.toString();
    }
}
