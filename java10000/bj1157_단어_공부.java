package java10000;

import java.util.Scanner;

public class bj1157_단어_공부 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int[] arr = new int[26];
        sc.close();
        for (int i = 0; i < str.length(); i++) {
            if (65 <= str.charAt(i) && str.charAt(i) <= 90) {
                arr[str.charAt(i) - 65] += 1;
            }
            else if (97 <= str.charAt(i) && str.charAt(i) <= 122) {
                arr[str.charAt(i) - 97] += 1;
            }
        }
        int max = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                ch = (char) (i + 65);
            } else if (arr[i] == max) {
                ch = '?';
            }
        }
        System.out.println(ch);
    }
}
