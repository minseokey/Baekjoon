class Solution {
    public int[] solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        for(int t: num_list){
            if(t % 2 == 0)
                even += 1;
            else
                odd += 1;
        }
        int[] ans = new int[2];
        ans[0] = even;
        ans[1] = odd;
        return ans;
    }
}