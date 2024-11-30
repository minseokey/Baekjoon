class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        answer += (int)hp/5;
        hp -= 5 * ((int)hp/5);
        answer += (int)hp/3;
        hp -= 3 * ((int)hp/3);
        answer += hp;
        return answer;
    }
}