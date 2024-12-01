import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string) {
        return my_string.toLowerCase()
                        .chars()
                        .sorted() 
                        .mapToObj(c -> String.valueOf((char) c))
                        .collect(Collectors.joining());
    }
}
