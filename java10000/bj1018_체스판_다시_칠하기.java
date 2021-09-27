package java10000;

import java.util.Scanner;

public class bj1018_체스판_다시_칠하기 {
    public static boolean[][] arr;
    public static int min = 64;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        arr = new boolean[n][m];
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                if (str.charAt(j) == 'W') {
                    arr[i][j] = true;
                } else {
                    arr[i][j] = false;
                }
            }
        }
        sc.close();
        int row_n = n - 7;
        int row_m = m - 7;

        for (int i = 0; i < row_n; i++) {
            for (int j = 0; j < row_m; j++) {
                find(i, j);
            }
        }
        System.out.println(min);
    }
    
    public static void find(int x, int y) {
        int end_x = x + 8;
        int end_y = y + 8;

        int cnt = 0;

        boolean temp = arr[x][y];

        for (int i = x; i < end_x; i++) {
            for (int j = y; j < end_y; j++) {
                if (arr[i][j] != temp) {
                    cnt += 1;
                }
                temp = (!temp);
            }
            temp = (!temp);
        }
        cnt = Math.min(cnt, 64 - cnt);

        min = Math.min(min, cnt);
    }
}
