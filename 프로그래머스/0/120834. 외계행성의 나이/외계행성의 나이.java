class Solution {
    public String solution(int age) {
        String ageStr = String.valueOf(age);
        StringBuilder str = new StringBuilder();
        for(char i: ageStr.toCharArray()){
            str.append((char)((int)i + 49));
        }
        return str.toString();
    }
}