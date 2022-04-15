package java10000;

import java.util.Scanner;

public class bj1259_팰린드롬수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            char[] arr = sc.nextLine().toCharArray();
            if (arr.length == 1) {
                if (arr[0] - '0' == 0) {
                    break;
                } else {
                    System.out.println("yes");
                }
            }
            int mid = arr.length / 2;

            for (int i = 0; i < mid; i++) {
                int start = arr[i] - '0';
                int reverse = arr[(arr.length - 1) - i] - '0';
                if (start != reverse) {
                    System.out.println("no");
                    break;
                }
                if (i == mid - 1) {
                    System.out.println("yes");
                }

            }
        }
        sc.close();
    }
}
