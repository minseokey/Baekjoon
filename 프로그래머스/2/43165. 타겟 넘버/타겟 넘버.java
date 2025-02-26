class Solution {
    static int ans;
    static int targetInd;
    static int targetNum;
    static int[] n_lis;
    
    public int solution(int[] numbers, int target) {
        targetInd = numbers.length;
        targetNum = target;
        n_lis = numbers;
        ans = 0;
        recur(0,0);
        
        return ans;
    }
    
    public void recur(int ind, int sum){
        if(ind == targetInd){
           if(sum == targetNum){
              ans += 1;
           }
        }
        else{
            recur(ind+1, sum-n_lis[ind]);
            recur(ind+1, sum+n_lis[ind]);
        }
    }
}