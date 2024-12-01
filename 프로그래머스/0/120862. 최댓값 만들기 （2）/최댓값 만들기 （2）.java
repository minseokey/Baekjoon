import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int[]numbersCopy = Arrays.copyOf(numbers, numbers.length);
        
        int maxPl = Arrays.stream(numbers).max().orElse(0);
        for(int i = 0; i < numbers.length; i ++){
            if(numbers[i] == maxPl){
                numbers[i] = -10001;
                break;
            }
        }
        int secMaxPl = Arrays.stream(numbers).max().orElse(0);

        int maxMi = Arrays.stream(numbersCopy).min().orElse(0);
        for(int i = 0; i < numbersCopy.length; i ++){
            if(numbersCopy[i] == maxMi){
                numbersCopy[i] = 10001;
                break;
            }
        }
        int secMaxMi = Arrays.stream(numbersCopy).min().orElse(0);
        return Math.max(maxPl*secMaxPl, maxMi*secMaxMi);
    }
}