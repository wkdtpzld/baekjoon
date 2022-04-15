package java10000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class bj3273_두_수의_합 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.valueOf(st.nextToken());
        }

        Arrays.sort(arr);

        int x = Integer.parseInt(br.readLine());
        int cnt = 0;
        int start = 0;
        int end = n - 1;
        int sum = 0;

        while (start < end) {
            sum = arr[start] + arr[end];
            if (sum == x) {
                cnt += 1;
                start += 1;
            }
            else if (sum < x) {
                start += 1;
            }
            else {
                end -= 1;
            }
        }
        System.out.println(cnt);
    }
}
