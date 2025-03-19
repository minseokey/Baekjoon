class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int MOD = 1000000007;
        int[][] field = new int[n][m];

        // 웅덩이 위치를 -1로 설정
        for (int[] puddle : puddles) {
            field[puddle[1] - 1][puddle[0] - 1] = -1;
        }

        // 시작점 초기화
        field[0][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (field[i][j] == -1) { // 웅덩이는 0으로 설정하여 경로 차단
                    field[i][j] = 0;
                    continue;
                }

                // 위쪽에서 오는 경우
                if (i > 0) {
                    field[i][j] = (field[i][j] + field[i - 1][j]) % MOD;
                }

                // 왼쪽에서 오는 경우
                if (j > 0) {
                    field[i][j] = (field[i][j] + field[i][j - 1]) % MOD;
                }
            }
        }

        return field[n - 1][m - 1];
    }
}
