class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(char t : my_string.toCharArray()){
            if(Character.isDigit(t)){
                answer += Character.getNumericValue(t);
            }
        }
        return answer;
    }
}