class Solution {
    public String solution(String my_string) {
        String tmp = my_string.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","");
        return tmp;
    }
}