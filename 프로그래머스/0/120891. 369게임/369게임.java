class Solution {
    public int solution(int order) {
        String arr = String.valueOf(order);
        int ans = 0;
        for(char tmp : arr.toCharArray()){
            if(tmp=='3'|| tmp=='6' || tmp=='9'){
                ans += 1;
            }
        }
        return ans;
    }
}