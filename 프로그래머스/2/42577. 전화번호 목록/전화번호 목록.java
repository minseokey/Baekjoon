import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
    Arrays.sort(phone_book);
        for(int j=0; j<phone_book.length-1; j++){
            if(phone_book[j].length() > phone_book[j+1].length()){
                if(phone_book[j].substring(0,phone_book[j+1].length()).equals(phone_book[j+1])){
                    return false;
                }
            }
            else{
                if(phone_book[j+1].substring(0,phone_book[j].length()).equals(phone_book[j])){
                    return false;
                }
            }
        }
        return true;
    }
}