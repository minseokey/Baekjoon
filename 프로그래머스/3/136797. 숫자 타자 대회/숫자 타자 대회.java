import java.util.*;

class Solution {
    static int[][] w = {
            {1, 7, 6, 7, 5, 4, 5, 3, 2, 3},
            {7, 1, 2, 4, 2, 3, 5, 4, 5, 6},
            {6, 2, 1, 2, 3, 2, 3, 5, 4, 5},
            {7, 4, 2, 1, 5, 3, 2, 6, 5, 4},
            {5, 2, 3, 5, 1, 2, 4, 2, 3, 5},
            {4, 3, 2, 3, 2, 1, 2, 3, 2, 3},
            {5, 5, 3, 2, 4, 2, 1, 5, 3, 2},
            {3, 4, 5, 6, 2, 3, 5, 1, 2, 4},
            {2, 5, 4, 5, 3, 2, 3, 2, 1, 2},
            {3, 6, 5, 4, 5, 3, 2, 4, 2, 1}
        };

    static int[][][] dp;
    static char[] numArr;

    public int solution(String numbers) {
        numArr = numbers.toCharArray();
        int n = numArr.length;
        
        dp = new int[n][10][10];
        for (int[][] d1 : dp) {
            for (int[] d2 : d1) {
                Arrays.fill(d2, -1);
            }
        }
        
        return recur(0, 4, 6);
    }

    private int recur(int ind, int left, int right) {
        if (ind == numArr.length) return 0;
        
        int target = numArr[ind] - '0';
        
        if (dp[ind][left][right] != -1) return dp[ind][left][right];

        int cost = Integer.MAX_VALUE;

        // 목표 숫자에 이미 손가락이 위치해 있다면, 반드시 그 손가락을 사용해야 함
        if (left == target) {
            return dp[ind][left][right] = recur(ind + 1, left, right) + 1;
        }
        if (right == target) {
            return dp[ind][left][right] = recur(ind + 1, left, right) + 1;
        }

        // 왼손이 target을 누를 경우
        int moveLeft = w[left][target] + recur(ind + 1, target, right);
        
        // 오른손이 target을 누를 경우
        int moveRight = w[right][target] + recur(ind + 1, left, target);

        // 최소 이동 비용을 저장
        return dp[ind][left][right] = Math.min(moveLeft, moveRight);
    }
}
