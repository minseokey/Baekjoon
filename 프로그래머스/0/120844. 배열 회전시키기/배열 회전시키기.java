class Solution {
    public int[] solution(int[] numbers, String direction) {
        if(direction.equals("right")){
            int last = numbers[numbers.length - 1];
            int[] newArr = new int[numbers.length];
            newArr[0] = last;
            for(int i = 0; i < numbers.length -1; i++){
                newArr[i+1] = numbers[i];
            }
            return newArr;
        }
        else{
            int first = numbers[0];
            int[] newArr = new int[numbers.length];
            newArr[numbers.length - 1] = first;
            for(int i = 0; i < numbers.length - 1; i++){
                newArr[i] = numbers[i+1];
            }
            return newArr;
        }
    }
}