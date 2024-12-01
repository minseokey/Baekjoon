class Solution {
    public int solution(int i, int j, int k) {
        int ans = 0;
        for(; i<=j; i++){
            String tmp = String.valueOf(i);
            ans += tmp.chars().filter(n -> n=='0'+k).count();
        }
        return ans;
    }
}