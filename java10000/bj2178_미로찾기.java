package java10000;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class bj2178_미로찾기 {

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
        for (int i = 0; i < n; i += 1) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j += 1) {
                arr[i][j] = str.charAt(j) - '0';
                visited[i][j] = 0;
            }
        }
        sc.close();
        visited[0][0] = 1;
        BFS(0, 0);
        System.out.println(arr[n - 1][m - 1]);
        
    }

    public static void BFS(int x, int y) {
        Queue<Dot> q = new LinkedList<Dot>();
        q.add(new Dot(x, y));

        while (!q.isEmpty()) {
            Dot d = q.poll();
            for (int i = 0; i < 4; i += 1) {
                int xx = d.x + dx[i];
                int yy = d.y + dy[i];

                if (xx < 0 || yy < 0 || xx >= n || yy >= m) {
                    continue;
                }
                if (visited[xx][yy] == 1 || arr[xx][yy] == 0) {
                    continue;
                }

                q.add(new Dot(xx, yy));

                arr[xx][yy] = arr[d.x][d.y] + 1;
                visited[xx][yy] = 1;
            }
        }
    }
}

class Dot {
    int x;
    int y;

    Dot(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

