class Solution {
    public String solution(String rsp) {
        char[] ans = new char[rsp.length()];
        int i = 0;
        for(char t : rsp.toCharArray()){
            switch (t){
                case '2':
                    ans[i++] = '0';
                    break;
                case '0':
                    ans[i++] = '5';
                    break;
                case '5':
                    ans[i++] = '2';
                    break;
            }
        }
        
        return String.valueOf(ans);
    }
}