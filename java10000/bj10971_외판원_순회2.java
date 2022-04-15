package java10000;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class bj10971_외판원_순회2 {

    static int N;
    static int[][] arr;
    static boolean[] visited;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());

        arr = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 1; i < N + 1; i++) {
            String[] s = br.readLine().split(" ");

            for (int j = 1; j < N + 1; j++) {
                arr[i][j] = Integer.parseInt(s[j - 1]);
            }
        }

        visited[1] = true;

        dfs(1, 1, 1, 0);
        bw.write(min + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
    
    public static void dfs(int start, int cur, int cnt, int cost) {
        if (cur == start && cost > 0) {
            min = Math.min(min, cost);
            return;
        }
        for (int i = 1; i < N + 1; i++) {
            
            if (arr[cur][i] != 0) {
                if (i == start && cnt == N) {
                    cost += arr[cur][i];
                    dfs(start, i, cnt + 1, cost);
                }
                else if(!visited[i]){
                    visited[i] = true;
                    cost += arr[cur][i];
    
                    dfs(start, i, cnt + 1, cost);
                    
                    cost -= arr[cur][i];
                    visited[i] = false;
                }
            }
            
        }
    }
}
