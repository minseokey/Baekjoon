class Solution {
    public String solution(String my_string) {
        char[] tmp = new char[my_string.length()];
        int i = 0;
        for(char a: my_string.toCharArray()){
            if(Character.isUpperCase(a)){
                tmp[i++] = Character.toLowerCase(a);
            }
            else{
                tmp[i++] = Character.toUpperCase(a);
            }
        }
        return String.valueOf(tmp);
    }
}