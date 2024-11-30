class Solution {
    public int solution(int n) {
        String tmp = Integer.toString(n);
        int ans = 0;
        for(char t : tmp.toCharArray()){
            ans += Character.getNumericValue(t);
        }
        return ans;
    }
}