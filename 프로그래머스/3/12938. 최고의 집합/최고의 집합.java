class Solution {
    public int[] solution(int n, int s) {
        int ret = s / n;
        int rem = s % n;
        if(ret == 0){
            return new int[]{-1};
        }
        else{
            int[] tmp = new int[n];
            for(int i = 0; i < n; i ++){
                tmp[i] = ret;
            }
            for(int i = n-1; i > n - rem - 1; i--){
                tmp[i] += 1;
            }
            return tmp;
        }
    }
}