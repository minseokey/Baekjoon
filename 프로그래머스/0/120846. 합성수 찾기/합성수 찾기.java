class Solution {
    public int solution(int n) {
        int ans = 0;
        for(int i = 4; i <= n; i ++){
            for(int j = 2; j < n; j++){
                if(i%j == 0 && i != j){
                    ans += 1;
                    break;
                }
            }
        }
        return ans;
    }
}