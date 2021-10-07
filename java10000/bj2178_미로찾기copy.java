package java10000;

import java.util.Queue;
import java.util.Scanner;
import java.util.LinkedList;

public class bj2178_미로찾기copy {
    static int[][] arr;
    static int[][] visited;
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };
    static int n;
    static int m;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();
        arr = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < arr.length; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < str.length(); j++) {
                arr[i][j] = str.charAt(j) - '0';
                visited[i][j] = 0;
            }
        }
        sc.close();
        visited[0][0] = 1;
        BFS(0, 0);
        System.out.println(arr[n-1][m-1]);

    }

    public static void BFS(int x, int y) {
        Queue<qq> queue = new LinkedList<>();
        queue.add(new qq(x, y));

        while (!(queue.isEmpty())) {
            qq d = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = d.x + dx[i];
                int ny = d.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }
                if (visited[nx][ny] == 1 || arr[nx][ny] == 0) {
                    continue;
                }
                queue.add(new qq(nx, ny));

                visited[nx][ny] = 1;
                arr[nx][ny] = arr[d.x][d.y] + 1;

            }
        }
    }
}

class qq {
    int x;
    int y;

    qq(int x, int y) {
        this.x = x;
        this.y = y;
    }
}