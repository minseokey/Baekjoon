import java.util.*;

class Solution {
    public String solution(String letter) {
        String[] splited = letter.split(" ");
        StringBuilder hi = new StringBuilder();
        for (String i : splited){
            switch (i){
                case ".-":
                    hi.append("a");
                    break;
                case "-...":
                    hi.append("b");
                    break;
                case "-.-.":
                    hi.append("c");
                    break;
                case "-..":
                    hi.append("d");
                    break;
                case ".":
                    hi.append("e");
                    break;
                case "..-.":
                    hi.append("f");
                    break;
                case "--.":
                    hi.append("g");
                    break;
                case "....":
                    hi.append("h");
                    break;
                case "..":
                    hi.append("i");
                    break;
                case ".---":
                    hi.append("j");
                    break;
                case "-.-":
                    hi.append("k");
                    break;
                case ".-..":
                    hi.append("l");
                    break;
                case "--":
                    hi.append("m");
                    break;
                case "-.":
                    hi.append("n");
                    break;
                case "---":
                    hi.append("o");
                    break;
                case ".--.":                    
                    hi.append("p");
                    break;
                case "--.-":
                    hi.append("q");
                    break;
                case ".-.":
                    hi.append("r");
                    break;
                case "...":
                    hi.append("s");
                    break;
                case "-":
                    hi.append("t");
                    break;
                case "..-":
                    hi.append("u");
                    break;
                case "...-":
                    hi.append("v");
                    break;
                case ".--":
                    hi.append("w");
                    break;
                case "-..-":
                    hi.append("x");
                    break;
                case "-.--":
                    hi.append("y");
                    break;
                case "--..":
                    hi.append("z");
                    break; 
            }
        }
        return hi.toString();
    }
}