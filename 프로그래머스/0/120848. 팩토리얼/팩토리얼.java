class Solution {
    public int solution(int n) {
        int tmp = 1;
        int ind = 1;
        while (true){
            tmp *= ind;
            if (tmp>n){
                break;
            }
            ind += 1;
        }
        return ind - 1;
    }
}