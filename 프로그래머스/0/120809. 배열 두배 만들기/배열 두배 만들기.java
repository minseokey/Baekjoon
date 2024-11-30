class Solution {
    public int[] solution(int[] numbers) {
        int[] ans = new int[numbers.length];
        int i = 0;
        for (int t: numbers){
            ans[i++] = t*2;
        }
        return ans;
    }
}