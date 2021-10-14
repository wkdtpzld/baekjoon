package java10000;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class bj10451_순열_사이클 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            ArrayList<ArrayList<Integer>> a = new ArrayList<>();
            for (int i = 0; i <= n; i++) {
                a.add(new ArrayList<>());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= n; i++) {
                int s = Integer.parseInt(st.nextToken());
                a.get(i).add(s);
            }
            boolean[] visited = new boolean[n + 1];
            int cnt = 0;
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    DFS(a, visited, i);
                    cnt++;
                }
            }
            System.out.println(cnt);
        }
        br.close();
        
    }
    
    public static void DFS(ArrayList<ArrayList<Integer>> a, boolean[] visited, int start) {
        for (int i : a.get(start)) {
            if (!visited[i]) {
                visited[i] = true;
                DFS(a, visited, i);
            }
        }
    }
}
