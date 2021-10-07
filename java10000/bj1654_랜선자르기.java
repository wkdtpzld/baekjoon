package java10000;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj1654_랜선자르기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] line = br.readLine().split(" ");
        int k = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);
        
        int[] inputArray = new int[k];
        for (int i = 0; i < inputArray.length; i++) {
            inputArray[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(inputArray);

        long end = inputArray[k - 1];
        long start = 1;
        long mid = 0;

        while (start <= end) {
            mid = (start + end) / 2;

            long cnt = 0;

            for (int i = 0; i < inputArray.length; i++) {
                cnt += inputArray[i] / mid;
            }

            if (cnt >= n) {
                start = mid + 1;
            } else if (cnt < n) {
                end = mid - 1;
            }
        }
        System.out.println(end);
    }
}
