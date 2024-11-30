class Solution {
    public int solution(int n, int t) {
        int ans = n;
        for(int i = 0; i < t; i ++){
            ans *= 2;
        }
        return ans;
    }
}