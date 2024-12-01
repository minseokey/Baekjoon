class Solution {
    public String solution(String my_string, int num1, int num2) {
        char w1 = my_string.charAt(num1);
        char w2 = my_string.charAt(num2);
        char[] charA = my_string.toCharArray();
        charA[num1] = w2;
        charA[num2] = w1;
        return String.valueOf(charA);
    }
}