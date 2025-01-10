import java.util.*;

class Solution {
    public int solution(int[] nums) {
        Map<Integer,Integer> cnt = new HashMap<>();
        for(int i = 0; i < nums.length; i ++){
            if(cnt.containsKey(nums[i])){
                cnt.replace(nums[i], cnt.get(nums[i]) + 1);
            }
            else{
                cnt.put(nums[i],1);
            }
        }
        
        if (cnt.keySet().size() > ((int)nums.length/2)){
            return (int)nums.length/2;
        }
        else{
            return cnt.keySet().size();
        }
    }
}