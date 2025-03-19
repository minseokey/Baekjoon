class Solution {
    public long solution(int[] sequence) {
        long[][] dp = new long[sequence.length][2];
        long tmp = 0;
        
        dp[0][0] = sequence[0];
        dp[0][1] = -sequence[0];
            
        for(int i = 1; i < sequence.length; i++){
            dp[i][0] = Math.max(dp[i-1][1] , 0) + sequence[i];
            dp[i][1] = Math.max(dp[i-1][0] , 0) - sequence[i];
        }
        
        for(long[] i : dp){
            tmp = Math.max(Math.max(i[0], i[1]), tmp);
        }
        return tmp;
    }
}
